# Use an official Python runtime as base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the bot script to the container
COPY bot.py .
COPY .env .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Run the bot
CMD ["python", "bot.py"]
