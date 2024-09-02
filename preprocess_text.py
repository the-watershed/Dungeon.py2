def preprocess_text(text):
    # Normalize line breaks
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

if __name__ == "__main__":
    pdf_path = "./resources/Fiend_Folio.pdf"
    text = extract_text_from_pdf(pdf_path)
    text = preprocess_text(text)
    with open("preprocessed_text.txt", "w") as text_file:
        text_file.write(text)
    print(text[:2000])  # Print the first 2000 characters for inspection
