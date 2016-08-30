FROM python:2-alpine
MAINTAINER Francisco Vaquero <akura11.tt@gmail.com>

RUN apk add git bash postgresql-dev gcc musl-dev python-dev --update-cache && rm -rf /var/cache/apk/*

RUN mkdir /project && \
    git clone https://github.com/vaquer/EncuestasDGM.git /project && \
    pip install -r /project/requirements.txt && \
    python project/EncuestasDGM/manage.py migrate && \
    python project/EncuestasDGM/encuestas/create_user_admin.py

EXPOSE 8001

CMD ["python", "project/EncuestasDGM/manage.py", "runserver", "0.0.0.0:8001"]