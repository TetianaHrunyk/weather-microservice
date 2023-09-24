FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
COPY ./schema.sql .


COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

WORKDIR /app
COPY ./src /app

ENV PYTHONPATH /app

EXPOSE 8000