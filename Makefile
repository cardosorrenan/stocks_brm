.DEFAULT_GOAL := all

COMPOSE=docker-compose $(COMPOSE_OPTS)

# help: display callable targets.
help:
	@egrep "^# " [Mm]akefile

# start:
start:
	$(COMPOSE) up -d

# build: 
build:
	$(COMPOSE) build

# down:
down:
	$(COMPOSE) down

# stop:
stop:
	$(COMPOSE) stop

# bash-api:
bash-api:
	$(COMPOSE) exec api bash

# bash-front: 
bash-front:
	$(COMPOSE) exec front bash

# migrate:
migrate:
	$(COMPOSE) exec api bash -c "\
		python manage.py makemigrations && \
		python manage.py migrate && \
		python manage.py loaddata dashboard/fixtures/*.json"

# clean-db:
clean-db:
	$(COMPOSE) exec api bash -c "python manage.py flush"

# logs-all:
logs-all:
	$(COMPOSE) logs --follow

# logs-api:
logs-api:
	$(COMPOSE) logs -f api

# logs-front:
logs-front:
	$(COMPOSE) logs -f api

# logs-db:
logs-db:
	$(COMPOSE) logs -f db

# test:
test:
	$(COMPOSE) exec api bash -c "pytest"

# rerun-local:
local-run:
	python stocks_brm-api/manage.py runserver 0.0.0.0:8005

# local-migrate
local-migrate:
	python stocks_brm-api/manage.py makemigrations
	python stocks_brm-api/manage.py migrate

# local-refresh:
local-refresh:
	python stocks_brm-api/manage.py flush
	python stocks_brm-api/manage.py loaddata stocks_brm-api/dashboard/fixtures/*.json
	python stocks_brm-api/manage.py runserver 0.0.0.0:8005