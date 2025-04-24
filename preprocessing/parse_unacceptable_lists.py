# preprocessing/parse_unacceptable_lists.py

"""
Extract text from any PDF
Clean ingredients names
Append new items to the master list without duplicates
"""

import re
import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() for page in reader.pages)
    return text

def extract_ingredient_names(text):
    raw_lines = text.split('\n')
    potential_names = []
    
    for line in raw_lines:
        if "CAS" in line or len(line.strip()) < 5:
            continue
        cleaned = re.sub(r'\s+', ' ', line)
        cleaned = re.sub(r'[^\w\s\-\(\),\']', '', cleaned).strip()
        if len(cleaned) > 3 and not cleaned.isnumeric():
            potential_names.append(cleaned)
    
    return set(potential_names)

def update_master_list(new_ingredients, master_list_path):
    # Load existing
    if os.path.exists(master_list_path):
        with open(master_list_path, 'r', encoding='utf-8') as f:
            existing = set(line.strip().lower() for line in f if line.strip())
    else:
        existing = set()
    
    # Combine and write back
    combined = sorted(existing.union({i.lower() for i in new_ingredients}))

    with open(master_list_path, 'w', encoding='utf-8') as f:
        for item in combined:
            f.write(item + "\n")
    
    print(f"Master list updated with {len(new_ingredients)} new items. Total: {len(combined)}")