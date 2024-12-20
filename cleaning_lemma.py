import re
import unicodedata

def normalize_text(text):
    """Normalize the text by removing diacritical marks."""
    normalized = unicodedata.normalize('NFD', text)
    return ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')

# Open and read the lemmatized input file
with open("lemmatized_text.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

# Extract the first word after each asterisk, normalize, and clean
cleaned_lemmas = []
for line in data:
    if line.startswith("*"):  # Ensure the line starts with an asterisk
        # Extract the first word after the asterisk
        match = re.match(r"\*\s*([^\s,]+)", line)
        if match:
            lemma = match.group(1)  # Get the first word
            normalized_lemma = normalize_text(lemma)  # Normalize the lemma
            cleaned_lemmas.append(normalized_lemma)

# Join all lemmas into a single cleaned text
final_text = " ".join(cleaned_lemmas)

# Write the cleaned and normalized text to a new file
with open("cleaned_normalized_text.txt", "w", encoding="utf-8") as file:
    file.write(final_text)

print("The cleaned and normalized text has been written to cleaned_normalized_text.txt.")
