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
ifdef APP
	@docker-compose logs -f $(APP)
else
	@docker-compose logs -f
endif

migrate:
	@docker-compose exec web python manage.py migrate --noinput

run: up migrate

reload:
ifdef APP
	@docker-compose stop $(APP)
	@docker-compose start $(APP)
else
	down up
endif