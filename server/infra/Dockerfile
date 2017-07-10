FROM python:slim

RUN apt-get update \
  && apt-get install build-essential libpcre3 libpcre3-dev -y

# basic flask environment
RUN pip3 install --upgrade pip qrcode flask pillow uwsgi

# application folder
ENV APP_DIR /app

RUN addgroup uwsgi \
  && useradd uwsgi -g uwsgi

# app dir
RUN mkdir ${APP_DIR} \
  && chown uwsgi:uwsgi ${APP_DIR} -R

WORKDIR ${APP_DIR}

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 5000

# copy config files into filesystem
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]