FROM alpine

# basic flask environment
RUN apk add --no-cache bash uwsgi uwsgi-python3 \
  && pip3 install --upgrade pip

# application folder
ENV APP_DIR /app

# app dir
RUN mkdir ${APP_DIR} \
  && chmod 777 /run/ -R \
  && chmod 777 /root/ -R
VOLUME [${APP_DIR}]
WORKDIR ${APP_DIR}

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

# copy config files into filesystem
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]