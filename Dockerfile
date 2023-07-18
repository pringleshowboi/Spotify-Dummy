# Specify the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the code files to the working directory
COPY inventory.py /app/inventory.py
COPY user.txt /app/

# Set the command to run the code
CMD ["python", "inventory.py"]
