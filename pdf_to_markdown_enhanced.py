#!/usr/bin/env python3
"""
Enhanced PDF to Markdown Converter with Design Preservation

This script converts PDF documents to markdown while preserving as much 
design and layout information as possible, including images, fonts, colors,
and spatial relationships.
"""

import os
import re
import sys
import base64
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from collections import defaultdict

try:
    import pdfplumber
except ImportError:
    print("pdfplumber not installed. Installing...")
    os.system("pip install pdfplumber")
    import pdfplumber

try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Installing...")
    os.system("pip install Pillow")
    from PIL import Image

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed. Installing...")
    os.system("pip install PyMuPDF")
    import fitz


class EnhancedPDFToMarkdownConverter:
    def __init__(self):
        self.output_dir = Path("markdown_output")
        self.images_dir = self.output_dir / "images"
        self.output_dir.mkdir(exist_ok=True)
        self.images_dir.mkdir(exist_ok=True)
        
        # Font size thresholds for header detection
        self.font_size_thresholds = {
            'h1': 18,
            'h2': 16,
            'h3': 14,
            'h4': 12,
            'body': 10
        }
        
    def extract_images_with_pymupdf(self, pdf_path: str, doc_name: str) -> Dict[int, List[str]]:
        """Extract images from PDF using PyMuPDF and save them."""
        images_by_page = defaultdict(list)
        
        try:
            doc = fitz.open(pdf_path)
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                image_list = page.get_images()
                
                for img_index, img in enumerate(image_list):
                    try:
                        # Get image data
                        xref = img[0]
                        pix = fitz.Pixmap(doc, xref)
                        
                        # Convert to PIL Image
                        if pix.n - pix.alpha < 4:  # GRAY or RGB
                            img_data = pix.tobytes("png")
                            img_filename = f"{doc_name}_page_{page_num + 1}_img_{img_index + 1}.png"
                            img_path = self.images_dir / img_filename
                            
                            with open(img_path, "wb") as f:
                                f.write(img_data)
                            
                            images_by_page[page_num].append(img_filename)
                            print(f"Extracted image: {img_filename}")
                        
                        pix = None  # Release memory
                        
                    except Exception as e:
                        print(f"Error extracting image {img_index} from page {page_num + 1}: {e}")
                        continue
            
            doc.close()
            
        except Exception as e:
            print(f"Error extracting images with PyMuPDF: {e}")
        
        return images_by_page
    
    def analyze_font_styles(self, page) -> Dict[str, Dict]:
        """Analyze font styles and sizes on a page for better formatting."""
        chars = page.chars
        font_analysis = defaultdict(lambda: {'count': 0, 'sizes': [], 'colors': []})
        
        for char in chars:
            font_name = char.get('fontname', 'unknown')
            font_size = char.get('size', 0)
            color = char.get('color', 0)  # May be None
            
            font_analysis[font_name]['count'] += 1
            font_analysis[font_name]['sizes'].append(font_size)
            if color is not None:
                font_analysis[font_name]['colors'].append(color)
        
        # Calculate average sizes for each font
        for font, data in font_analysis.items():
            data['avg_size'] = sum(data['sizes']) / len(data['sizes']) if data['sizes'] else 0
            data['max_size'] = max(data['sizes']) if data['sizes'] else 0
            data['min_size'] = min(data['sizes']) if data['sizes'] else 0
        
        return dict(font_analysis)
    
    def detect_headers_with_font_info(self, text_objects: List[Dict]) -> List[Dict]:
        """Enhanced header detection using font size and style information."""
        processed_objects = []
        
        for obj in text_objects:
            text = obj.get('text', '').strip()
            if not text:
                continue
                
            font_size = obj.get('size', 12)
            font_name = obj.get('fontname', '')
            
            # Determine markdown header level based on font size
            header_level = None
            if font_size >= self.font_size_thresholds['h1']:
                header_level = 1
            elif font_size >= self.font_size_thresholds['h2']:
                header_level = 2
            elif font_size >= self.font_size_thresholds['h3']:
                header_level = 3
            elif font_size >= self.font_size_thresholds['h4']:
                header_level = 4
            
            # Additional heuristics for header detection
            is_bold = 'bold' in font_name.lower() or 'black' in font_name.lower()
            is_short = len(text.split()) <= 10
            is_title_case = text.istitle() or text.isupper()
            
            if header_level and (is_bold or is_title_case or is_short):
                obj['markdown_type'] = 'header'
                obj['header_level'] = header_level
            else:
                obj['markdown_type'] = 'paragraph'
            
            processed_objects.append(obj)
        
        return processed_objects
    
    def extract_text_with_layout(self, pdf_path: str) -> Tuple[str, Dict]:
        """Extract text with detailed layout and styling information."""
        content_parts = []
        doc_metadata = {}
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                doc_metadata['total_pages'] = len(pdf.pages)
                
                for page_num, page in enumerate(pdf.pages, 1):
                    print(f"Processing page {page_num}/{len(pdf.pages)} with layout analysis")
                    
                    # Analyze font styles on this page
                    font_analysis = self.analyze_font_styles(page)
                    
                    # Extract text objects with positioning
                    chars = page.chars
                    words = page.extract_words()
                    
                    # Group words into text objects
                    text_objects = []
                    current_line = []
                    current_y = None
                    
                    for word in words:
                        word_y = word.get('top', 0)
                        
                        # If we're on a new line (different y position)
                        if current_y is None or abs(word_y - current_y) > 2:
                            if current_line:
                                # Process current line
                                line_text = ' '.join([w['text'] for w in current_line])
                                if line_text.strip():
                                    avg_size = sum([w.get('size', 12) for w in current_line]) / len(current_line)
                                    text_objects.append({
                                        'text': line_text,
                                        'size': avg_size,
                                        'fontname': current_line[0].get('fontname', ''),
                                        'x0': min([w.get('x0', 0) for w in current_line]),
                                        'y0': current_line[0].get('top', 0),
                                        'color': current_line[0].get('color', 0)
                                    })
                            current_line = [word]
                            current_y = word_y
                        else:
                            current_line.append(word)
                    
                    # Don't forget the last line
                    if current_line:
                        line_text = ' '.join([w['text'] for w in current_line])
                        if line_text.strip():
                            avg_size = sum([w.get('size', 12) for w in current_line]) / len(current_line)
                            text_objects.append({
                                'text': line_text,
                                'size': avg_size,
                                'fontname': current_line[0].get('fontname', ''),
                                'x0': min([w.get('x0', 0) for w in current_line]),
                                'y0': current_line[0].get('top', 0),
                                'color': current_line[0].get('color', 0)
                            })
                    
                    # Detect headers and format text
                    formatted_objects = self.detect_headers_with_font_info(text_objects)
                    
                    # Extract tables
                    tables = page.extract_tables()
                    
                    # Build page content
                    page_content = [f"\n<!-- Page {page_num} -->\n"]
                    
                    # Add formatted text objects
                    for obj in formatted_objects:
                        text = self.clean_text(obj['text'])
                        if not text:
                            continue
                            
                        if obj.get('markdown_type') == 'header':
                            level = obj.get('header_level', 3)
                            page_content.append(f"{'#' * level} {text}\n")
                        else:
                            # Check for special formatting
                            if obj.get('size', 12) < 10:
                                page_content.append(f"<small>{text}</small>\n")
                            else:
                                page_content.append(f"{text}\n")
                    
                    # Add tables
                    for table in tables:
                        if table:
                            table_md = self.format_table_as_markdown(table)
                            page_content.append(f"\n{table_md}\n")
                    
                    content_parts.extend(page_content)
        
        except Exception as e:
            print(f"Error in layout extraction: {e}")
            return "", {}
        
        return "\n".join(content_parts), doc_metadata
    
    def clean_text(self, text: str) -> str:
        """Enhanced text cleaning with better formatting preservation."""
        if not text:
            return ""
        
        # Preserve intentional spacing but clean up excessive whitespace
        # Replace multiple spaces with single space, but preserve line breaks
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        
        # Fix common PDF extraction issues
        replacements = {
            '\u2019': "'",      # Smart quote
            '\u2018': "'",      # Smart quote
            '\u201c': '"',      # Smart quote
            '\u201d': '"',      # Smart quote
            '\u2013': '-',      # En dash
            '\u2014': '--',     # Em dash
            '\u00a0': ' ',      # Non-breaking space
            '\u2022': '•',      # Bullet point
            '\u25cf': '•',      # Black circle
            '\u25cb': '○',      # White circle
            '\u2026': '...',    # Ellipsis
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text.strip()
    
    def format_table_as_markdown(self, table: List[List[str]]) -> str:
        """Enhanced table formatting with better alignment."""
        if not table or not table[0]:
            return ""
        
        # Clean table data
        cleaned_table = []
        for row in table:
            cleaned_row = [self.clean_text(str(cell or "")) for cell in row]
            cleaned_table.append(cleaned_row)
        
        if not cleaned_table:
            return ""
        
        # Determine column count
        max_cols = max(len(row) for row in cleaned_table)
        
        # Normalize all rows to have the same number of columns
        for row in cleaned_table:
            while len(row) < max_cols:
                row.append("")
        
        # Build markdown table
        markdown_lines = []
        
        # Header row
        headers = cleaned_table[0]
        markdown_lines.append("| " + " | ".join(headers) + " |")
        
        # Separator row with alignment
        separators = []
        for header in headers:
            if header.strip():
                separators.append("---")
            else:
                separators.append("---")
        markdown_lines.append("| " + " | ".join(separators) + " |")
        
        # Data rows
        for row in cleaned_table[1:]:
            if any(cell.strip() for cell in row):  # Skip empty rows
                markdown_lines.append("| " + " | ".join(row) + " |")
        
        return "\n".join(markdown_lines)
    
    def generate_css_styles(self, doc_metadata: Dict) -> str:
        """Generate CSS styles for enhanced rendering."""
        css = """
<style>
/* Enhanced PDF-to-Markdown Styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.3em;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    border: 1px solid #ddd;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #f8f9fa;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.page-break {
    page-break-before: always;
    border-top: 2px dashed #ccc;
    margin: 2em 0;
    padding-top: 1em;
}

small {
    font-size: 0.85em;
    color: #666;
}

blockquote {
    border-left: 4px solid #ddd;
    margin: 1em 0;
    padding-left: 1em;
    color: #666;
}

.image-container {
    text-align: center;
    margin: 1em 0;
}

.image-container img {
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
"""
        return css
    
    def convert_pdf_to_enhanced_markdown(self, pdf_path: str) -> Optional[str]:
        """Convert PDF to markdown with enhanced design preservation."""
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            print(f"File not found: {pdf_path}")
            return None
        
        print(f"Converting with enhanced design preservation: {pdf_path.name}")
        doc_name = pdf_path.stem
        
        # Extract images first
        print("Extracting images...")
        images_by_page = self.extract_images_with_pymupdf(str(pdf_path), doc_name)
        
        # Extract text with layout analysis
        print("Analyzing layout and extracting text...")
        text_content, doc_metadata = self.extract_text_with_layout(str(pdf_path))
        
        if not text_content:
            print(f"Failed to extract content from {pdf_path.name}")
            return None
        
        # Generate output filename
        output_name = f"{doc_name}_enhanced.md"
        output_path = self.output_dir / output_name
        
        # Build enhanced markdown content
        css_styles = self.generate_css_styles(doc_metadata)
        
        # Add images to content where appropriate
        enhanced_content = text_content
        for page_num, image_files in images_by_page.items():
            page_marker = f"<!-- Page {page_num + 1} -->"
            if page_marker in enhanced_content:
                image_htmls = []
                for img in image_files:
                    image_htmls.append(f'<div class="image-container">')
                    image_htmls.append(f'<img src="images/{img}" alt="Image from page {page_num + 1}">')
                    image_htmls.append(f'</div>')
                image_html = "\n".join(image_htmls)
                enhanced_content = enhanced_content.replace(
                    page_marker, 
                    f"{page_marker}\n{image_html}"
                )
        
        # Create final document
        final_content = f"""{css_styles}

# {doc_name}

> **Enhanced Conversion** from PDF: `{pdf_path.name}`  
> Conversion date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
> Pages: {doc_metadata.get('total_pages', 'Unknown')}  
> Images extracted: {sum(len(imgs) for imgs in images_by_page.values())}  

---

{enhanced_content}

---

*This document was converted using the Enhanced PDF to Markdown Converter, which preserves layout, styling, and images from the original PDF.*
"""
        
        # Write to file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            print(f"✅ Enhanced conversion successful: {output_path}")
            print(f"📁 Images saved in: {self.images_dir}")
            print(f"🎨 Includes CSS styling for enhanced rendering")
            
            return str(output_path)
            
        except Exception as e:
            print(f"Error writing enhanced file: {e}")
            return None
    
    def convert_all_pdfs_enhanced(self, directory: str = ".") -> List[str]:
        """Convert all PDF files with enhanced design preservation."""
        directory = Path(directory)
        pdf_files = list(directory.glob("*.pdf"))
        
        if not pdf_files:
            print("No PDF files found in the current directory.")
            return []
        
        print(f"Found {len(pdf_files)} PDF files for enhanced conversion:")
        for pdf in pdf_files:
            print(f"  - {pdf.name}")
        
        converted_files = []
        for pdf_file in pdf_files:
            result = self.convert_pdf_to_enhanced_markdown(pdf_file)
            if result:
                converted_files.append(result)
        
        return converted_files


def main():
    """Main function with options for basic or enhanced conversion."""
    if len(sys.argv) > 1 and sys.argv[1] == "--enhanced":
        print("🎨 Starting Enhanced PDF to Markdown Conversion")
        print("Features: Layout preservation, image extraction, font analysis, CSS styling")
        
        converter = EnhancedPDFToMarkdownConverter()
        
        if len(sys.argv) > 2:
            # Convert specific file
            pdf_path = sys.argv[2]
            converter.convert_pdf_to_enhanced_markdown(pdf_path)
        else:
            # Convert all PDFs in current directory
            converted = converter.convert_all_pdfs_enhanced()
            
            print(f"\n🎉 Enhanced conversion complete!")
            print(f"Converted {len(converted)} files:")
            for file in converted:
                print(f"  ✅ {file}")
            
            if converted:
                print(f"\n📁 Enhanced markdown files saved in: {converter.output_dir.absolute()}")
                print(f"🖼️  Images saved in: {converter.images_dir.absolute()}")
                print(f"💡 Open the .md files in a markdown viewer that supports HTML/CSS for best results")
    else:
        print("Usage:")
        print("  python pdf_to_markdown_enhanced.py --enhanced              # Convert all PDFs with design preservation")
        print("  python pdf_to_markdown_enhanced.py --enhanced file.pdf     # Convert specific PDF with design preservation")
        print("\nThe enhanced mode preserves:")
        print("  • Font sizes and styles for better header detection")
        print("  • Images and graphics")
        print("  • Table formatting and alignment")
        print("  • Layout information")
        print("  • CSS styling for enhanced rendering")


if __name__ == "__main__":
    main() 