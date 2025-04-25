# Use the official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 5000

# Start the app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
