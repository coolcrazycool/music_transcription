FROM python:3.6.10
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

EXPOSE 8000

CMD gunicorn -w 4 hyper_music.wsgi:application -b :8000
