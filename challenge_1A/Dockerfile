# Use slim Python image for size and AMD64 compatibility
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other code (main.py, app/, etc.)
COPY . .

# Set command to run your main script
CMD ["python", "main.py"]