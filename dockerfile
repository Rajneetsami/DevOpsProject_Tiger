# Dockerfile example
FROM python:3.11-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV API_KEY=${API_KEY}  # This references the API_KEY environment variable from Azure

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose the port Flask will run on
EXPOSE 5000

# Command to run Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
