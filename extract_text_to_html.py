import fitz  # PyMuPDF

def extract_text_from_pdf_to_html(pdf_path, output_html_path):
    document = fitz.open(pdf_path)
    html_content = "<html><body>"

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        html_content += page.get_text("html")

    html_content += "</body></html>"

    with open(output_html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    pdf_path = "./resources/Monster_Manual_1.pdf"
    output_html_path = "extracted_text.html"
    extract_text_from_pdf_to_html(pdf_path, output_html_path)
    print(f"Extracted text has been saved to {output_html_path}")
