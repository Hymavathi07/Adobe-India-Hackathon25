import fitz  # PyMuPDF
import os

def extract_sections(input_dir):
    all_sections = []
    for filename in os.listdir(input_dir):
        if not filename.endswith(".pdf"):
            continue
        doc = fitz.open(os.path.join(input_dir, filename))
        for page_num in range(len(doc)):
            page = doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" not in block:
                    continue
                text = ""
                for line in block["lines"]:
                    for span in line["spans"]:
                        text += span["text"].strip() + " "
                if len(text.strip()) > 30:  # Skip short lines
                    all_sections.append({
                        "document": filename,
                        "page": page_num + 1,
                        "section_title": text.strip(),
                        "text": text.strip()
                    })
    return all_sections
