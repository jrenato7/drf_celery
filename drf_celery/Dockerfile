# pull official base image
FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY ./requirements/libs.txt /requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./start_celeryworker.sh /start_celeryworker.sh
RUN sed -i 's/\r$//g' /start_celeryworker.sh
RUN chmod +x /start_celeryworker.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]