import fitz  # PyMuPDF
import os
import json
from pathlib import Path

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace(".pdf", "")
    headings = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = ""
                font_sizes = []
                for span in line["spans"]:
                    line_text += span["text"].strip() + " "
                    if span["size"] > 4:
                        font_sizes.append(span["size"])

                if line_text.strip() == "":
                    continue

                if font_sizes:
                    avg_font_size = sum(font_sizes) / len(font_sizes)

                    if avg_font_size > 17:
                        level = "H1"
                    elif avg_font_size > 14:
                        level = "H2"
                    elif avg_font_size > 11:
                        level = "H3"
                    else:
                        continue

                    headings.append({
                        "level": level,
                        "text": line_text.strip(),
                        "page": page_num + 1
                    })

    return {
        "title": title,
        "outline": headings
    }

def main():
    base_dir = Path(__file__).resolve().parent
    input_dir = base_dir / "app" / "input"
    output_dir = base_dir / "app" / "output"

    # ✅ Ensure input folder exists
    if not input_dir.exists():
        print(f"❌ ERROR: Folder not found → {input_dir}")
        print("👉 Please create this folder and add at least one PDF file.")
        return

    # ✅ Create output folder if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    found = False
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            found = True
            pdf_path = input_dir / filename
            result = extract_outline(pdf_path)
            json_path = output_dir / filename.replace(".pdf", ".json")

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"✅ Extracted: {filename} → {json_path}")

    if not found:
        print("⚠️ No PDF files found in the input folder.")

if __name__ == "__main__":
    main()
