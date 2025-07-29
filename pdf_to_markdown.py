#!/usr/bin/env python3
"""
PDF to Markdown Converter

This script converts PDF documents to markdown format with proper formatting,
handling headers, paragraphs, lists, and other common document structures.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Optional

try:
    import pdfplumber
except ImportError:
    print("pdfplumber not installed. Installing...")
    os.system("pip install pdfplumber")
    import pdfplumber

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 not installed. Installing...")
    os.system("pip install PyPDF2")
    import PyPDF2


class PDFToMarkdownConverter:
    def __init__(self):
        self.output_dir = Path("markdown_output")
        self.output_dir.mkdir(exist_ok=True)
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize extracted text."""
        if not text:
            return ""
        
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Fix common PDF extraction issues
        text = text.replace('\u2019', "'")  # Smart quotes
        text = text.replace('\u2018', "'")
        text = text.replace('\u201c', '"')
        text = text.replace('\u201d', '"')
        text = text.replace('\u2013', '-')  # En dash
        text = text.replace('\u2014', '--')  # Em dash
        text = text.replace('\u00a0', ' ')  # Non-breaking space
        
        return text.strip()
    
    def detect_headers(self, text: str, font_info: dict = None) -> str:
        """Detect and format headers based on text patterns and font info."""
        lines = text.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Detect headers based on common patterns
            if (len(line) < 100 and 
                (line.isupper() or 
                 any(keyword in line.lower() for keyword in ['overview', 'introduction', 'conclusion', 'summary']) or
                 re.match(r'^\d+\.?\s+[A-Z]', line) or  # Numbered headers
                 (not line.endswith('.') and len(line.split()) < 10))):
                
                # Determine header level
                if line.isupper() or any(word in line.lower() for word in ['overview', 'introduction']):
                    formatted_lines.append(f"# {line}")
                elif re.match(r'^\d+\.?\s+', line):
                    formatted_lines.append(f"## {line}")
                else:
                    formatted_lines.append(f"### {line}")
            else:
                formatted_lines.append(line)
        
        return '\n\n'.join(formatted_lines)
    
    def format_lists(self, text: str) -> str:
        """Format bullet points and numbered lists."""
        lines = text.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append("")
                continue
            
            # Detect bullet points
            if re.match(r'^[•·▪▫‣⁃]\s+', line):
                formatted_lines.append(f"- {line[2:].strip()}")
            elif re.match(r'^[\-\*]\s+', line):
                formatted_lines.append(line)
            elif re.match(r'^\d+[\.\)]\s+', line):
                # Numbered lists
                formatted_lines.append(line)
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def extract_text_pdfplumber(self, pdf_path: str) -> str:
        """Extract text using pdfplumber (better for structured content)."""
        text_content = []
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    print(f"Processing page {page_num}/{len(pdf.pages)}")
                    
                    # Extract text
                    page_text = page.extract_text()
                    if page_text:
                        # Clean and add page separator
                        cleaned_text = self.clean_text(page_text)
                        if cleaned_text:
                            text_content.append(f"<!-- Page {page_num} -->\n\n{cleaned_text}")
                    
                    # Extract tables if any
                    tables = page.extract_tables()
                    for table in tables:
                        if table:
                            table_md = self.format_table_as_markdown(table)
                            text_content.append(f"\n\n{table_md}\n\n")
        
        except Exception as e:
            print(f"Error extracting with pdfplumber: {e}")
            return ""
        
        return "\n\n".join(text_content)
    
    def format_table_as_markdown(self, table: List[List[str]]) -> str:
        """Convert table data to markdown format."""
        if not table or not table[0]:
            return ""
        
        markdown_table = []
        
        # Header row
        headers = [cell or "" for cell in table[0]]
        markdown_table.append("| " + " | ".join(headers) + " |")
        markdown_table.append("| " + " | ".join(["---"] * len(headers)) + " |")
        
        # Data rows
        for row in table[1:]:
            if row:
                cells = [str(cell or "") for cell in row]
                # Pad with empty cells if row is shorter than header
                while len(cells) < len(headers):
                    cells.append("")
                markdown_table.append("| " + " | ".join(cells) + " |")
        
        return "\n".join(markdown_table)
    
    def extract_text_pypdf2(self, pdf_path: str) -> str:
        """Fallback text extraction using PyPDF2."""
        text_content = []
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    print(f"Processing page {page_num}/{len(pdf_reader.pages)}")
                    
                    page_text = page.extract_text()
                    if page_text:
                        cleaned_text = self.clean_text(page_text)
                        if cleaned_text:
                            text_content.append(f"<!-- Page {page_num} -->\n\n{cleaned_text}")
        
        except Exception as e:
            print(f"Error extracting with PyPDF2: {e}")
            return ""
        
        return "\n\n".join(text_content)
    
    def convert_pdf_to_markdown(self, pdf_path: str) -> Optional[str]:
        """Convert a single PDF to markdown."""
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            print(f"File not found: {pdf_path}")
            return None
        
        print(f"Converting: {pdf_path.name}")
        
        # Try pdfplumber first (better for structured content)
        text = self.extract_text_pdfplumber(str(pdf_path))
        
        # Fallback to PyPDF2 if pdfplumber fails
        if not text:
            print("Falling back to PyPDF2...")
            text = self.extract_text_pypdf2(str(pdf_path))
        
        if not text:
            print(f"Failed to extract text from {pdf_path.name}")
            return None
        
        # Format the text as markdown
        text = self.detect_headers(text)
        text = self.format_lists(text)
        
        # Generate output filename
        output_name = pdf_path.stem + ".md"
        output_path = self.output_dir / output_name
        
        # Add document header
        markdown_content = f"""# {pdf_path.stem}

> Converted from PDF: {pdf_path.name}
> Conversion date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

{text}
"""
        
        # Write to file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"✅ Converted successfully: {output_path}")
            return str(output_path)
        except Exception as e:
            print(f"Error writing file: {e}")
            return None
    
    def convert_all_pdfs(self, directory: str = ".") -> List[str]:
        """Convert all PDF files in the specified directory."""
        directory = Path(directory)
        pdf_files = list(directory.glob("*.pdf"))
        
        if not pdf_files:
            print("No PDF files found in the current directory.")
            return []
        
        print(f"Found {len(pdf_files)} PDF files:")
        for pdf in pdf_files:
            print(f"  - {pdf.name}")
        
        converted_files = []
        for pdf_file in pdf_files:
            result = self.convert_pdf_to_markdown(pdf_file)
            if result:
                converted_files.append(result)
        
        return converted_files


def main():
    """Main function to run the PDF to Markdown converter."""
    converter = PDFToMarkdownConverter()
    
    if len(sys.argv) > 1:
        # Convert specific file
        pdf_path = sys.argv[1]
        converter.convert_pdf_to_markdown(pdf_path)
    else:
        # Convert all PDFs in current directory
        converted = converter.convert_all_pdfs()
        
        print(f"\n🎉 Conversion complete!")
        print(f"Converted {len(converted)} files:")
        for file in converted:
            print(f"  ✅ {file}")
        
        if converted:
            print(f"\nMarkdown files saved in: {converter.output_dir.absolute()}")


if __name__ == "__main__":
    main() 