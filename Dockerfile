# # Use an official Python runtime as the base image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file to the working directory
# COPY requirements.txt .

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the Django project code to the working directory
# COPY . .

# #Set environment variables
# ENV DJANGO_SETTINGS_MODULE=BS.settings
# ENV PYTHONUNBUFFERED=1

# # Expose the port on which the Django app will run
# EXPOSE 8000

# # Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]