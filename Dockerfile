FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the calculator.py script from local file system into the container
COPY calculator.py /app/calculator.py

# Install any required Python packages (if needed)
# RUN pip3 install <package-name>

#Ensure script have execute permission
RUN chmod+x /app/calculator.py

# Set the default command to execute calculator.py
CMD ["python3", "/app/calculator.py"]
