# Pull base image for python
FROM python:3.8-slim

# Set the working directory in the image
WORKDIR /app

#Copy everything needed from the current directory
COPY . .

# This is the Another way to copy the directory is
# Copy the requirements file into the image
# COPY requirements.txt /app/requirements.txt

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]


