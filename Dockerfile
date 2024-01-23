# Stage 1: Build the application
FROM python:3.8-slim AS builder

# Set the working directory in the builder stage
WORKDIR /app

# Copy only the requirements file to the builder stage
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the final image
FROM python:3.8-slim

# Set the working directory in the final stage
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY app.py .
COPY templates templates

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

