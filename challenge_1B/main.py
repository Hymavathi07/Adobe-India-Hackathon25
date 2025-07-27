from extractor import extract_sections
from ranker import rank_sections
import json
import os
from datetime import datetime

def load_query():
    with open("app/persona_job.json") as f:
        return json.load(f)

def save_output(data):
    output_path = "app/output/output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    query = load_query()
    all_sections = extract_sections("app/input")
    ranked_sections = rank_sections(all_sections, query["persona"], query["job_to_be_done"])

    metadata = {
        "documents": list(set([s["document"] for s in all_sections])),
        "persona": query["persona"],
        "job_to_be_done": query["job_to_be_done"],
        "timestamp": datetime.now().isoformat()
    }

    output = {
        "metadata": metadata,
        "extracted_sections": ranked_sections,
        "sub_section_analysis": []  # Can fill later
    }

    save_output(output)
    print("✅ Output saved to app/output/output.json")

if __name__ == "__main__":
    main()
