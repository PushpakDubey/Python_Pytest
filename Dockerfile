# Purpose: Dockerfile for Python Pytest
# Creator: Pushpak Dubey
# Use official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

LABEL authors="pushpakdubey"

# Command to run the tests
CMD ["pytest", "tests/test_calculator.py", "-v"]