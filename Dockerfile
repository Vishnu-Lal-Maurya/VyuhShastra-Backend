# Use a base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

# Start the application using gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
