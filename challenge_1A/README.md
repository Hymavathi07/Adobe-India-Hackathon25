#  Adobe Hackathon 2025 - Round 1A: PDF Outline Extractor

## Challenge Overview

The goal of this project is to automatically extract a **structured outline** from any given PDF.  
Specifically, the solution extracts:

- **Title**
- **Headings** with levels:
  - H1
  - H2
  - H3
- Each heading is tagged with its **page number**

This outline is returned in a valid JSON format and will be used as the base for later stages in the hackathon.

---

##  Problem Statement

Given a PDF of up to 50 pages:

- Detect the **Title** and structured headings (H1, H2, H3)
- Output the result as a valid JSON file
- Should work **offline** and be run **inside Docker**
- **No network**, **no APIs**, and **model (if used) ≤ 200MB**

---

##  Key Features

- Extracts:
  - PDF Title (from filename)
  - Headings and subheadings (H1, H2, H3) using text + font size
  - Page numbers for each heading
- Produces clean, hierarchical JSON format
- Works **offline**
- Fully Dockerized
- Compatible with AMD64 (CPU only)

---

##  Folder Structure

<img width="470" height="221" alt="image" src="https://github.com/user-attachments/assets/efd83499-256b-49c2-b463-b741958ef919" />

---

##  Technologies Used

- **Python 3.9**
- **PyMuPDF (fitz)** – for PDF parsing
- **Docker** – to containerize and run the solution offline
- **VS Code** – development environment

---

##  Setup Instructions

### 🔹 Prerequisites

Make sure these tools are installed:
- Python 3.9+
- Docker Desktop (for AMD64 CPUs)
- Git
- VS Code (recommended)

---

### 🔹 Run Locally (Without Docker)

1. Open terminal in the root project folder
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt

---
### 🔹 Run with Docker (As Required for Submission)
1. Build Docker Image:
   ```bash
    docker build --platform linux/amd64 -t pdf-extractor:submission .
2. Run Docker Container:
   ```bash
    docker run --rm \
      -v ${PWD}/app/input:/app/input \
      -v ${PWD}/app/output:/app/output \
      --network none pdf-extractor:submission
---

###  Sample JSON Output Format
<img width="728" height="577" alt="image" src="https://github.com/user-attachments/assets/8ae5b916-131e-4fce-8b80-d426b2ab83f8" />

---

##  Approach
- Used PyMuPDF to parse PDF pages and extract text spans
- Based on font size, classified text blocks into:
      - H1 → Larger size (typically > 17)
      - H2 → Medium (14–17)
      - H3 → Small headers (11–14)
- Avoided relying only on fixed fonts or positions to keep it general
- Output structure is created using Python dictionaries and dumped as JSON

---

##  Constraints Handled
Constraint	Status
- PDF size ≤ 50 pages	✅ Yes
- Execution time ≤ 10s	✅ Yes
- No internet access	✅ Yes
- Model size ≤ 200MB	✅ Not used
- CPU only (AMD64)	✅ Yes
- Output JSON format	✅ Yes
- Docker-compatible	✅ Yes

---

##  Dependencies
- PyMuPDF==1.23.7
- Install locally with:
      - pip install -r requirements.txt


