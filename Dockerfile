# Use a Python image with version 3.10
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    ffmpeg \
    x11-utils \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files into the container
COPY main.py .
COPY gui.py .
COPY visualization.py .
COPY frequency_analysis.py .
COPY audio_processing.py .
COPY constants.py .

# Set environment variable to connect to the host's display
ENV DISPLAY=${DISPLAY}

# Command to run the application
CMD ["python", "main.py"]
