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

def parse_monster_data(text):
    monsters = []
    # Regular expression to match each monster block
    monster_pattern = re.compile(
        r"([A-Z\s\(\)-]+)\n"  # Monster name in all caps and possibly with parentheses
        r"(.*?LEVEL/X\.P\. VALUE: .*?)\n"  # Traits block including LEVEL/X.P. VALUE
        r"(.*?)(?=[A-Z\s\(\)-]+\n|$)",  # Description until the next monster name or end of text
        re.DOTALL
    )
    
    for match in monster_pattern.finditer(text):
        name = match.group(1).strip()
        traits_block = match.group(2).strip()
        description = match.group(3).strip()
        
        # Extract individual traits
        traits = {}
        trait_lines = traits_block.split('\n')
        current_trait = None
        for line in trait_lines:
            if ':' in line:
                key, value = line.split(':', 1)
                current_trait = key.strip()
                traits[current_trait] = value.strip()
            elif current_trait:
                traits[current_trait] += ' ' + line.strip()
        
        monster = {
            "name": name,
            "traits": traits,
            "description": description
        }
        monsters.append(monster)
    
    return monsters

if __name__ == "__main__":
    pdf_path = "./resources/Fiend_Folio.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    # Parse the extracted text to get monster data
    monsters = parse_monster_data(text)
    
    # Write the monster data to a JSON file
    with open("monsters.json", "w") as json_file:
        json.dump(monsters, json_file, indent=4)
    
    # Optionally, print the first few monsters for inspection
    print(json.dumps(monsters[:2], indent=4))
