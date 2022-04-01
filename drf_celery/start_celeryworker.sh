#!/bin/bash

set -o errexit
set -o nounset

celery -A drf_celery worker -l INFO