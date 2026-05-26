FROM python:3.10-slim

# Install system dependencies (including ffmpeg for audio processing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file first to utilize Docker build cache
COPY requirements.txt .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port (Render/Koyeb/Hugging Face inject $PORT)
EXPOSE 8080

# Command to run the bot
CMD ["python", "main.py"]
