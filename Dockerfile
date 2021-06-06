FROM python:3.8-slim-buster as base
RUN apt-get update && apt-get install -y netcat


WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh ./
RUN chmod +x entrypoint.sh
CMD bash /app/entrypoint.sh api-db
