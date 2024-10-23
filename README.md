### `README.md`

# PDF Manipulation Tool

A command-line Python application for manipulating PDF files. This tool allows users to extract specific pages from a PDF and save them as a new file. The tool can be extended to include additional PDF operations, such as merging, rotating, and splitting PDFs.

## Features

- Extract pages from a PDF and save them as a new PDF file.
- Command-line interface (CLI) for easy usage directly from the terminal.

## Prerequisites

- Python 3.8+
- `PyPDF2` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/pdf-manipulation-tool.git
   cd pdf-manipulation-tool
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies:**

   Run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To extract pages from a PDF file, you can use the following command:

```bash
python pdf_tool.py <source_pdf> <output_pdf> <start_page> <end_page>
```

### Example

To extract pages 48 to 83 from `LSD.pdf` and save them to `LSD_cut.pdf`, use:

```bash
python pdf_tool.py LSD.pdf LSD_cut.pdf 48 83
```

This command will create a new PDF file `LSD_cut.pdf` containing pages 48 to 83 of `LSD.pdf`.

## Arguments

- `source_pdf`: The path to the source PDF file.
- `output_pdf`: The path where the new PDF with the extracted pages will be saved.
- `start_page`: The starting page number (1-based).
- `end_page`: The ending page number (1-based).

## Error Handling

- If the source PDF file does not exist, the tool will output an error message.
- If the page range is invalid (e.g., out of bounds), the tool will notify the user and terminate the operation.

## Future Enhancements

- **Merging PDFs**: Add the ability to merge multiple PDF files.
- **Splitting PDFs**: Split a PDF into individual pages or multiple ranges.
- **Rotating Pages**: Rotate pages within the PDF.
- **Watermarking PDFs**: Add a watermark to specific pages.
