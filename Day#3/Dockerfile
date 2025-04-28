# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and source code
COPY . /app

# Install necessary libraries
RUN pip install pandas scikit-learn

# Run the Python script
CMD ["python", "main.py"]
