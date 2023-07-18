# Specify the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the code files to the working directory
COPY requirements.txt /app/

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory to the working directory
COPY . /app/

# Set the command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
