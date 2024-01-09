FROM python:3.10-slim AS builder

RUN mkdir /usr/src/app
COPY ./my-app /usr/src/app
COPY requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install numpy

ENV URL=postgres://user:password@localhost:5432/database

EXPOSE 5000

CMD ["python", "app.py"]


