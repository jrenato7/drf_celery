FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install dependencies
COPY requirements.txt /requirements.txt

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