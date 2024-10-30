FROM python:3.12

# Environment variables to improve Docker behavior
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents Python from writing .pyc files
ENV PYTHONUNBUFFERED 1         # Ensures stdout and stderr are sent directly to the terminal

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

# Copy the entire project directory to the working directory
COPY . /code/
