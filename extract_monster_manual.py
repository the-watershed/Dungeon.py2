import fitz  # PyMuPDF
import re
import json

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
    return text

if __name__ == "__main__":
    pdf_path = "./resources/Monster_Manual_1.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    # Debugging output: Print the first 5000 characters of the extracted text
    print("Extracted text from PDF:")
    print(text[:5000])
