FROM python:3.7

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /newapp 
WORKDIR /newapp
COPY ./newapp /newapp

RUN adduser user
USER user

