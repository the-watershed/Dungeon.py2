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

def preprocess_text(text):
    # Normalize line breaks
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

def parse_monster_data(text):
    monsters = []
    # Split the text into sections based on some delimiter or pattern
    sections = text.split("Monster Name:")  # Adjust this based on actual text structure
    for section in sections[1:]:  # Skip the first split part as it will be empty
        monster = {}
        # Extract the name
        name_match = re.search(r"^(.*?)\s", section)
        if name_match:
            monster["name"] = name_match.group(1).strip()
        # Extract stats
        stats_match = re.search(r"Stats:\s(.*?)\s", section)
        if stats_match:
            monster["stats"] = stats_match.group(1).strip()
        # Extract abilities
        abilities_match = re.search(r"Abilities:\s(.*?)\s", section)
        if abilities_match:
            monster["abilities"] = abilities_match.group(1).strip()
        # Extract description
        description_match = re.search(r"Description:\s(.*?)\s", section)
        if description_match:
            monster["description"] = description_match.group(1).strip()
        # Extract hit dice
        hit_dice_match = re.search(r"Hit Dice:\s(.*?)\s", section)
        if hit_dice_match:
            monster["hit_dice"] = hit_dice_match.group(1).strip()
        if monster:
            monsters.append(monster)
    
    return monsters

def save_to_json(data, json_path):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    pdf_path = "./resources/Fiend_Folio.pdf"
    json_path = "monsters.json"
    
    text = extract_text_from_pdf(pdf_path)
    text = preprocess_text(text)
    print("Extracted text length:", len(text))  # Debugging statement
    monsters = parse_monster_data(text)
    print("Number of monsters extracted:", len(monsters))  # Debugging statement
    save_to_json(monsters, json_path)

if __name__ == "__main__":
    main()
