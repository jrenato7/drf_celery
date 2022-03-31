clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

up: clean
	@docker-compose up -d --build

down:
	@docker-compose down -v --remove-orphans

start:
	@docker-compose start

stop:
	@docker-compose stop

logs:
	@docker-compose logs -f

migrate:
	@docker-compose exec drf_celery python manage.py migrate --noinput

run: up migrate
