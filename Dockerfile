FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD gunicorn vg_site.wsgi:application --bind 0.0.0.0:$PORT