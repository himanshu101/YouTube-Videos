FROM python:3.7-alpine

COPY ./requirements.txt .
RUN set -e; \
       	apk add --no-cache --virtual .build-deps \
       		gcc \
       		libc-dev \
       		linux-headers \
       		mariadb-dev;
RUN set -e;	\
    pip install --upgrade pip; \
	pip install -r requirements.txt;
COPY ./src /app
WORKDIR /app
RUN mkdir log
CMD [ "uwsgi", "--ini", "locallibrary/app.ini" ]