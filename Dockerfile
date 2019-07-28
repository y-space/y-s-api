
# y-s-api

FROM frolvlad/alpine-python-machinelearning
RUN apk add --update --no-cache gcc g++ wget python3-dev

RUN mkdir /app
RUN mkdir /app/y-s-datasets
RUN mkdir /app/y-s-datasets/exoplanets
RUN mkdir /app/y-s-datasets/messier
RUN mkdir /app/y-s-datasets/tess
WORKDIR /app

RUN pip install astropy
RUN pip install gunicorn flask flask-cors

COPY api.py api.py
COPY wsgi.py wsgi.py
COPY y-s-datasets/exoplanets/exoplanets.json y-s-datasets/exoplanets/exoplanets.json
COPY y-s-datasets/exoplanets/exoplanets-stats.json y-s-datasets/exoplanets/exoplanets-stats.json
COPY y-s-datasets/messier/messier.json y-s-datasets/messier/messier.json
COPY y-s-datasets/tess/tess.json y-s-datasets/tess/tess.json

EXPOSE 7799

ENTRYPOINT gunicorn -b :7799 --access-logfile - --error-logfile - wsgi

