FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the calculator.py script into the container
COPY calculator.py /app/calculator.py

# Install any required Python packages (if needed)
# RUN pip3 install <package-name>

# Set the default command to execute calculator.py
CMD ["python3", "/app/calculator.py"]
