# PDF to Markdown Converter

A Python script that converts PDF documents to well-formatted Markdown files.

## Features

- **Dual PDF Processing**: Uses both `pdfplumber` (primary) and `PyPDF2` (fallback) for robust text extraction
- **Smart Header Detection**: Automatically detects and formats headers based on text patterns
- **List Formatting**: Converts bullet points and numbered lists to proper Markdown syntax
- **Table Support**: Extracts and converts tables to Markdown table format
- **Text Cleaning**: Handles common PDF extraction issues like smart quotes and special characters
- **Page Tracking**: Includes page numbers as HTML comments for reference
- **Metadata**: Adds conversion timestamp and source file information

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

### Convert All PDFs in Current Directory
```bash
python pdf_to_markdown.py
```

### Convert a Specific PDF
```bash
python pdf_to_markdown.py "path/to/your/file.pdf"
```

## Output

- Converted markdown files are saved in the `markdown_output/` directory
- Original PDF filenames are preserved with `.md` extension
- Each markdown file includes:
  - Document title as main header
  - Conversion metadata
  - Page separators for reference
  - Properly formatted content with headers, lists, and tables

## Example Output Structure

```
markdown_output/
├── Document1.md
├── Document2.md
└── Document3.md
```

## Dependencies

- `pdfplumber>=0.7.0` - Primary PDF text extraction
- `PyPDF2>=3.0.0` - Fallback PDF processing
- `pathlib` - Path handling

## Converted Documents

This repository contains the following converted LinkedIn OAuth documentation:

1. **Authenticating with OAuth 2.0 Overview** - General OAuth 2.0 concepts for LinkedIn API
2. **LinkedIn 3-Legged OAuth Flow** - Detailed implementation guide for member authorization
3. **Share on LinkedIn** - Documentation for sharing content via LinkedIn API

All original PDF files and their converted Markdown versions are included in this repository.

## License

MIT License - Feel free to use and modify as needed. 