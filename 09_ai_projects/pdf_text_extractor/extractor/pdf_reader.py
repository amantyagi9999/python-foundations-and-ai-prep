import PyPDF2
import pdfplumber

def extract_text_from_pdf(pdf_path):
    text_output = []
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            text_output.append(f"--- Page {page_num + 1} ---\n{text}\n")
    return "\n".join(text_output)

def extract_text_pdfplumber(pdf_path):
    text_output = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            text_output.append(f"--- Page {i + 1} ---\n{text}\n")
    return "\n".join(text_output)
