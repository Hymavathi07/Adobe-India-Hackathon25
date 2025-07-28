# Adobe-India-Hackathon25

This repository includes solutions for:
  -  **Challenge 1A: PDF Outline Extraction**
  -  **Challenge 1B: Persona-Driven Document Intelligence**

> **Connecting the Dots Through Docs**  
> Reimagining how PDFs are read, understood, and navigated.

---
##  Challenge 1A — PDF Processing & Structured Outline Extraction

###  Objective
Extract structured outlines from raw PDFs using local, fast, and reliable techniques.

###  Folder Structure
<img width="376" height="229" alt="image" src="https://github.com/user-attachments/assets/8c71de00-4313-4489-a5ef-8c736c71de69" />

###  Features
- Extracts table of contents from a PDF
- Converts PDF structure to JSON format
- Runs inside a Docker container
- Fast and scalable

###  How to Run (Locally)
    ```bash
      pip install -r requirements.txt
      python main.py

##  Docker Instructions
    ```bash
    docker build -t pdfoutline:latest .
    docker run -it --rm pdfoutline:latest

##  Output
Outputs JSON files with structured outline under app/output/.

---

###  Challenge 1B — Persona-Driven Document Intelligence

 ## Objective
Given a set of PDFs, extract and rank sections most relevant to a specific persona and their job-to-be-done.

##  Folder Structure
    ```bash
    challenge_1B/
    ├── app/
    │   ├── input/              # Input PDFs
    │   ├── output/             # Final JSON output
    ├── extractor.py            # PDF content extractor
    ├── ranker.py               # Relevance scoring engine
    ├── persona_job.json        # Input prompt for persona and job
    ├── main.py                 # Execution pipeline
    ├── requirements.txt
    ├── Dockerfile
    └── README.md

###  Input Format
    persona_job.json should contain:
    ```bash
    {
      "persona": "Investment Analyst",
      "job_to_be_done": "Analyze revenue trends, R&D investments, and market positioning strategies"
    }

###  Features
 1. Extracts section titles and context from all PDFs in app/input/
 2. Uses Sentence-BERT for semantic matching with persona & job
 3. Produces ranked section list with metadata + sub-section analysis
 4. Offline, fast, CPU-only inference

###  How to Run (Locally)
    ```bash
      pip install -r requirements.txt
      python main.py
##  Docker Instructions
    ```bash
      docker build --platform linux/amd64 -t persona_ranker:latest .
      docker run --rm -v $(pwd)/app/input:/app/input -v $(pwd)/app/output:/app/output --network none               persona_ranker:latest
###  Output
Structured JSON in app/output/output.json with:
  1. Document name, page number
  2.  Ranked relevant sections
  3.  Sub-section insights
  4.  Timestamp & persona metadata




