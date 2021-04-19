# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /opt/app/

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8100


CMD ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]