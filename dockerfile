# Use the official Python image from the Docker Hub
FROM python:3.11-slim

ARG API_KEY
ENV API_KEY=${API_KEY}
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5001
EXPOSE 5001

# Specify the command to run the application
CMD ["python", "app.py"]
