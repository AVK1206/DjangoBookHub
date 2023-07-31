FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production
RUN mkdir /app

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations

EXPOSE 8000

