# PDF to Markdown Converter

A comprehensive Python toolkit that converts PDF documents to well-formatted Markdown files with two conversion modes: **Basic** and **Enhanced Design Preservation**.

## 🆕 Two Conversion Modes

### Basic Conversion (`pdf_to_markdown.py`)
- Fast text extraction and basic formatting
- Good for simple documents

### Enhanced Conversion (`pdf_to_markdown_enhanced.py`) 
- **🎨 Design Preservation**: Maintains visual hierarchy and layout
- **🖼️ Image Extraction**: Automatically extracts and embeds images
- **📐 Font Analysis**: Uses font size/style for intelligent header detection
- **🎯 Layout Analysis**: Preserves spatial relationships and positioning
- **💅 CSS Styling**: Includes beautiful CSS for enhanced rendering

## Core Features

- **Dual PDF Processing**: Uses both `pdfplumber` (primary) and `PyPDF2` (fallback) for robust text extraction
- **Smart Header Detection**: Font-based header detection with configurable size thresholds
- **List Formatting**: Converts bullet points and numbered lists to proper Markdown syntax
- **Table Support**: Extracts and converts tables to Markdown table format with proper alignment
- **Text Cleaning**: Handles common PDF extraction issues like smart quotes and special characters
- **Page Tracking**: Includes page numbers as HTML comments for reference
- **Image Preservation**: Extracts diagrams, charts, and images (Enhanced mode)
- **CSS Integration**: Professional styling for web/print rendering (Enhanced mode)

## Installation

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Conversion
```bash
# Convert all PDFs in current directory
python pdf_to_markdown.py

# Convert specific PDF
python pdf_to_markdown.py "filename.pdf"
```

### Enhanced Conversion (Recommended)
```bash
# Convert all PDFs with design preservation
python pdf_to_markdown_enhanced.py --enhanced

# Convert specific PDF with design preservation
python pdf_to_markdown_enhanced.py --enhanced "filename.pdf"
```

## Output

### Basic Conversion Output
- Files saved as `filename.md` in `markdown_output/` directory
- Simple text-based markdown with basic formatting

### Enhanced Conversion Output  
- Files saved as `filename_enhanced.md` in `markdown_output/` directory
- **CSS Styling**: Embedded CSS for professional rendering
- **Images**: Extracted to `markdown_output/images/` directory
- **Font Analysis**: Headers detected based on actual font sizes
- **Layout Preservation**: Spatial relationships maintained

Each markdown file includes:
- Document title as main header
- Conversion metadata (timestamp, page count, image count)
- Page separators for reference
- Properly formatted content with headers, lists, and tables
- Embedded images (Enhanced mode)

## Example Output Structure

```
markdown_output/
├── Document1.md                    # Basic conversion
├── Document1_enhanced.md           # Enhanced conversion
├── Document2_enhanced.md
├── Document3_enhanced.md
└── images/                         # Extracted images
    ├── Document1_page_2_img_1.png
    ├── Document1_page_3_img_1.png
    └── Document2_page_1_img_1.png
```

## Dependencies

- `pdfplumber>=0.7.0` - Primary PDF text extraction with layout analysis
- `PyPDF2>=3.0.0` - Fallback PDF processing
- `PyMuPDF>=1.23.0` - Image extraction and advanced PDF processing (Enhanced mode)
- `Pillow>=9.1.0` - Image processing and manipulation (Enhanced mode)
- `pathlib` - Path handling

## 🎨 Design Preservation Features

The Enhanced mode preserves PDF design elements including:

### Visual Hierarchy
- **Font Size Analysis**: Detects headers based on actual font sizes from PDF
- **Font Style Detection**: Identifies bold, italic, and special formatting
- **Smart Thresholds**: Configurable font size thresholds for header levels

### Layout & Spacing
- **Line Positioning**: Maintains spatial relationships between elements
- **Column Detection**: Handles multi-column layouts
- **Text Flow**: Preserves paragraph structure and spacing

### Visual Elements
- **Image Extraction**: Automatically extracts diagrams, charts, and graphics
- **Table Formatting**: Enhanced table detection with proper alignment
- **CSS Styling**: Professional web-ready styling with responsive design

### Enhanced Output
- **Embedded CSS**: Beautiful styling for markdown viewers
- **Image Integration**: Seamlessly embedded images with captions
- **Metadata Rich**: Detailed conversion information and statistics

## Converted Documents

This repository contains the following converted LinkedIn OAuth documentation:

1. **Authenticating with OAuth 2.0 Overview** - General OAuth 2.0 concepts for LinkedIn API
2. **LinkedIn 3-Legged OAuth Flow** - Detailed implementation guide with 5 extracted diagrams
3. **Share on LinkedIn** - Documentation for sharing content via LinkedIn API

All original PDF files, basic conversions, and enhanced conversions with extracted images are included in this repository.

### Conversion Results
- **3 LinkedIn OAuth PDFs** → **Basic + Enhanced Markdown**
- **5 Images Extracted** from OAuth Flow documentation
- **CSS-Styled Enhanced Versions** for professional presentation

## License

MIT License - Feel free to use and modify as needed. 