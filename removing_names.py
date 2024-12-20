import re

# Open the original name file
with open("roman_names.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Remove brackets and their contents
cleaned_data = re.sub(r"\[\d+\]", "", data)

# Remove all commas
cleaned_data = cleaned_data.replace(",", "")

# Write the cleaned data to a new file
with open("cleaned_roman_names.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_data.strip())

print("The cleaned name list has been saved as 'cleaned_roman_names.txt'.")
