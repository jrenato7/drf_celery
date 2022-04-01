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
ifdef ARGS
	@docker-compose logs -f $(ARGS)
else
	@docker-compose logs -f
endif

migrate:
	@docker-compose exec drf_celery python manage.py migrate --noinput

run: up migrate

reload: down up