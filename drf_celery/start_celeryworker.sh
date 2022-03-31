#!/bin/sh

set -o errexit
set -o nounset

cd /app/drf_celery/

celery -A drf_celery worker -l INFO