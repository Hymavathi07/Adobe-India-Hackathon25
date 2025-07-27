# 🧠 Adobe Hackathon 2025 - Round 1A: PDF Outline Extractor

## 📘 Challenge Overview

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

## 🎯 Problem Statement

Given a PDF of up to 50 pages:

- Detect the **Title** and structured headings (H1, H2, H3)
- Output the result as a valid JSON file
- Should work **offline** and be run **inside Docker**
- **No network**, **no APIs**, and **model (if used) ≤ 200MB**

---

## ✅ Key Features

- Extracts:
  - PDF Title (from filename)
  - Headings and subheadings (H1, H2, H3) using text + font size
  - Page numbers for each heading
- Produces clean, hierarchical JSON format
- Works **offline**
- Fully Dockerized
- Compatible with AMD64 (CPU only)

---

## 📁 Folder Structure

pdf-outline-extractor/
├── app/
│ ├── input/    **#** Place your PDF files here
│ ├── output/   **#** Extracted outline JSON files will appear here
├── main.py     **#** Python script to extract PDF outlines
├── requirements.txt   **#** Python dependencies
├── Dockerfile   **#** Docker container config
├── README.md    **#** Project documentation

---

## 🛠️ Technologies Used

- **Python 3.9**
- **PyMuPDF (fitz)** – for PDF parsing
- **Docker** – to containerize and run the solution offline
- **VS Code** – development environment

---

## 🔧 Setup Instructions

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

## Place any .pdf file inside:
app/input/

## Run the script:
python main.py

## Output .json will appear in:
app/output/

## Build Docker Image
docker build --platform linux/amd64 -t pdf-extractor:submission .

## Run Docker Container
docker run --rm \
  -v ${PWD}/app/input:/app/input \
  -v ${PWD}/app/output:/app/output \
  --network none pdf-extractor:submission

## This command:
- Processes all .pdf files inside /app/input/
- Outputs matching .json files inside /app/output/

---

### 🔍 Sample JSON Output Format
<img width="766" height="881" alt="image" src="https://github.com/user-attachments/assets/6a7687dd-569b-4ac2-974f-cc2d4bd14cca" />

---

## 🧠 Approach
- Used PyMuPDF to parse PDF pages and extract text spans
- Based on font size, classified text blocks into:
      - H1 → Larger size (typically > 17)
      - H2 → Medium (14–17)
      - H3 → Small headers (11–14)
- Avoided relying only on fixed fonts or positions to keep it general
- Output structure is created using Python dictionaries and dumped as JSON

---

## ⚙️ Constraints Handled
Constraint	Status
- PDF size ≤ 50 pages	✅ Yes
- Execution time ≤ 10s	✅ Yes
- No internet access	✅ Yes
- Model size ≤ 200MB	✅ Not used
- CPU only (AMD64)	✅ Yes
- Output JSON format	✅ Yes
- Docker-compatible	✅ Yes

---

## 📝 Dependencies
- PyMuPDF==1.23.7
- Install locally with:
      - pip install -r requirements.txt


