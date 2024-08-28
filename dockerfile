# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Set environment variables for the superuser
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run migrations
#RUN  python manage.py migrate
#RUN python manage.py createsuperuser --noinput

# Collect static files
#RUN python manage.py collectstatic --noinput

# Define environment variable
ENV DJANGO_ENV=production

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

