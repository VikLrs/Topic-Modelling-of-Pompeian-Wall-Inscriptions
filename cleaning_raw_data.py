import re

def extract_cil_number(publication_line):
    """Extract the CIL number from the publication line."""
    match = re.search(r"CIL 04, \*?(\d+)", publication_line)
    if match:
        return int(match.group(1))
    return None

def is_in_valid_range(cil_number):
    """Check if the CIL number is within the valid ranges."""
    return (
        (1 <= cil_number <= 1162) or
        (1205 <= cil_number <= 2502) or
        (2885 <= cil_number <= 3255) or
        (3341 <= cil_number <= 3879) or
        (3881 <= cil_number <= 3883) or
        (3885 <= cil_number <= 5423) or
        (6601 <= cil_number <= 6690) or
        (6697 <= cil_number <= 6865) or
        (7008 <= cil_number <= 7107)
    )

# Open and read the input file
with open("edcs_raw_data.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Split data into individual inscriptions
inscriptions = data.strip().split("\n\n")

# List to store the Latin text
latin_texts = []

for inscription in inscriptions:
    # Check if the inscription mentions "CIL 04"
    if "CIL 04" in inscription:
        material_match = re.search(r"material: (.+)", inscription, re.IGNORECASE)
        material = material_match.group(1).strip().lower() if material_match else None

        include_inscription = False
        if material in ["tectorium", "lapis"]:
            include_inscription = True
        elif not material:
            publication_line_match = re.search(r"publication: (.+)", inscription, re.IGNORECASE)
            if publication_line_match:
                publication_line = publication_line_match.group(1)
                cil_number = extract_cil_number(publication_line)
                if cil_number and is_in_valid_range(cil_number):
                    include_inscription = True

        if include_inscription:
            # Extract Latin text
            latin_start = re.search(r"province: Latium et Campania / Regio I\s+place: Pompei", inscription)
            if latin_start:
                latin_text_section = inscription[latin_start.end():].strip()
                latin_lines = []
                for line in latin_text_section.split("\n"):
                    if ":" in line or not line.strip():
                        break
                    latin_lines.append(line.strip())
                if latin_lines:
                    latin_texts.append("\n".join(latin_lines))

# Clean the text by removing parentheses and brackets while keeping their contents
cleaned_texts = []
for text in latin_texts:
    cleaned_text = re.sub(r"[\[\]()]", "", text)  # Corrected the regex
    cleaned_texts.append(cleaned_text)

# Write the cleaned Latin text to an output file
with open("edcs_cleaned_data.txt", "w", encoding="utf-8") as file:
    file.write("\n\n".join(cleaned_texts))

print("Cleaned Latin text has been written to edcs_cleaned_data.txt.")
