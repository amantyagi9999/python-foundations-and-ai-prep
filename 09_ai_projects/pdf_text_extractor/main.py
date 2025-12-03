from extractor.pdf_reader import extract_text_from_pdf, extract_text_pdfplumber

PDF_PATH = "/Users/amant/Desktop/Interview Doc/DSA revision guide.pdf"   # Add your PDF file here

if __name__ == "__main__":
    print("Extracting using PyPDF2...")
    text1 = extract_text_from_pdf(PDF_PATH)
    print(text1)

    print("\nExtracting using pdfplumber...")
    text2 = extract_text_pdfplumber(PDF_PATH)
    print(text2)
