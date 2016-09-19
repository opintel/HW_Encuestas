FROM python:2-alpine
MAINTAINER Francisco Vaquero <akura11.tt@gmail.com>

RUN apk add git bash postgresql-dev gcc musl-dev python-dev --update-cache && rm -rf /var/cache/apk/*

RUN mkdir /project && \
    git clone -b dev --single-branch https://github.com/opintel/HW_Encuestas.git /project && \
    pip install -r /project/requirements.txt

EXPOSE 8001
ADD start.sh /start.sh

ENTRYPOINT /start.sh