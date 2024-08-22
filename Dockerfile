# Use an official Python 3.12 runtime as a base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local content into the container at /app
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV DATA_DIR=/app/documents
ENV COLLECTION_NAME=my_documents

# Define the command to run the application
CMD ["python", "app/main.py"]

