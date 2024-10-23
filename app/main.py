import argparse
import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pages_from_pdf(source_pdf_path, output_pdf_path, start_page, end_page):
    """Extract pages from a source PDF and save them as a new PDF."""
    try:
        reader = PdfReader(source_pdf_path)
        writer = PdfWriter()
        
        # Ensure the page range is within bounds
        total_pages = len(reader.pages)
        if start_page < 1 or end_page > total_pages or start_page > end_page:
            raise ValueError(f"Invalid page range: PDF has {total_pages} pages.")
        
        # Extract the specified pages
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])
        
        # Write the new PDF
        with open(output_pdf_path, 'wb') as output_pdf:
            writer.write(output_pdf)
        
        print(f"Pages {start_page} to {end_page} extracted from {source_pdf_path} to {output_pdf_path}")
    
    except FileNotFoundError:
        print(f"Error: File '{source_pdf_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract specific pages from a PDF file.")
    
    parser.add_argument('source_pdf', help="Path to the source PDF file.")
    parser.add_argument('output_pdf', help="Path to save the output PDF file.")
    parser.add_argument('start_page', type=int, help="The start page number (1-based).")
    parser.add_argument('end_page', type=int, help="The end page number (1-based).")

    # Parse arguments from command line
    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.isfile(args.source_pdf):
        print(f"Error: The source PDF file '{args.source_pdf}' does not exist.")
        return

    # Extract pages from PDF
    extract_pages_from_pdf(args.source_pdf, args.output_pdf, args.start_page, args.end_page)

if __name__ == "__main__":
    print("Running")
    main()
