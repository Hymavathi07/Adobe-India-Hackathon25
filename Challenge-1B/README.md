# 📄 Challenge 1B: Persona-Driven Document Intelligence

##  Objective
Build an intelligent document analyst that can extract and prioritize the most relevant sections from a collection of PDFs, based on:
- A **specific persona**
- A **job-to-be-done**

This system helps users quickly find the information that matters to them — enabling **focused, personalized document comprehension**.

---

##  Problem Statement

Given:
- A **collection of 3–10 domain-specific PDF documents**
- A **persona** (e.g., Student, Researcher, Analyst, etc.)
- A **job-to-be-done** (e.g., Summarize R&D trends, Identify exam topics, etc.)

You must:
1. Parse and analyze the content of all PDFs
2. Extract and rank the most relevant **sections and sub-sections**
3. Return a well-structured `output.json` with all extracted metadata and content

---

##  Input Format

All inputs reside under: `app/input/`

- **PDF Files**  
  Multiple `.pdf` documents (3–10)

- **Persona + Job File**  
  A JSON file named `persona_job.json`, containing:
  ```json
  {
    "persona": "Investment Analyst",
    "job_to_be_done": "Analyze revenue trends, R&D investments, and market positioning strategies"
  }

###  Output Format
Your output is generated as app/output/output.json, structured as:
<img width="1506" height="631" alt="image" src="https://github.com/user-attachments/assets/219f398a-27db-4a2b-a434-49c0a91b1c03" />

---

### Project Structure
<img width="342" height="341" alt="image" src="https://github.com/user-attachments/assets/a4e81089-fba7-4bbd-8b3b-299a8cd2c913" />

---

###  How to Run Locally (Without Docker)
✅ Install dependencies
    ```bash
    pip install -r requirements.txt
✅ Place PDFs & persona_job.json inside app/input/
✅ Run main script
    ```bash
      python main.py
✅ View the output at app/output/output.json

###  Docker Instructions
✅ Build Docker Image
    ```bash
      docker build --platform linux/amd64 -t persona_ranker:<your_name> .
✅ Run Docker Container
    ```bash
      docker run --rm \
        -v $(pwd)/app/input:/app/input \
        -v $(pwd)/app/output:/app/output \
        --network none \
        persona_ranker:<your_name>

---

###  Constraints
✅ Must run CPU-only
✅ Total model size ≤ 1 GB
✅ Total processing time ≤ 60 seconds (for 3–5 PDFs)
🚫 No internet access during execution




