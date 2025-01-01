FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV TEMPLATES_AUTO_RELOAD=True

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache
    
# Run the application
CMD ["python", "app.py"]
