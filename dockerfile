# Dockerfile example
FROM python:3.11-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV API_KEY=  # Leave it empty, as the value will be injected at runtime

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port 5001 (Flask will run on this port)
EXPOSE 5001

# Command to run Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
