FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get install -y python-pip python-dev build-essential
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/