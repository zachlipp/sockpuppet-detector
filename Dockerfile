FROM python:3.11-slim

WORKDIR home

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

COPY tests tests

ENTRYPOINT uvicorn --host 0.0.0.0 --port 1337 main:app
# ENTRYPOINT pytest
