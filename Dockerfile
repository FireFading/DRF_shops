FROM python:3.11.0-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN python -m pip install --upgrade pip -r requirements.txt

EXPOSE 8000