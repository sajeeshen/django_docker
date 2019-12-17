FROM python:3.7-alpine
MAINTAINER Sajeesh
ENV PYTHONUNBUFFERED 1
COPY /requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev

RUN apk --update add \
    postgresql-dev gcc python3-dev musl-dev \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    # pillow dependencies \
    jpeg-dev \
    zlib-dev

RUN pip install -r /requirements.txt
RUN mkdir /app

WORKDIR /app
copy ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN chmod -R 755 /vol/web
