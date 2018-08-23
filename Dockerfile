
# y-s-api

FROM python:3.7-alpine

RUN mkdir /app
RUN mkdir /app/y-s-datasets
RUN mkdir /app/y-s-datasets/exoplanets
RUN mkdir /app/y-s-datasets/messier
WORKDIR /app

RUN pip install gunicorn flask flask-cors

COPY api.py api.py
COPY wsgi.py wsgi.py
COPY y-s-datasets/exoplanets/exoplanets.json y-s-datasets/exoplanets/exoplanets.json
COPY y-s-datasets/messier/messier.json y-s-datasets/messier/messier.json

EXPOSE 7799

ENTRYPOINT gunicorn -b :7799 --access-logfile - --error-logfile - wsgi

