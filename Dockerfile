FROM python:3.8.3
MAINTAINER HyperProject Inc

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get install -y lilypond

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD gunicorn hyper_music.wsgi:application --bind 0.0.0.0:$PORT
