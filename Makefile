.DEFAULT_GOAL := all

COMPOSE=docker-compose $(COMPOSE_OPTS)

# help: display callable targets.
help:
	@egrep "^# " [Mm]akefile

# up:
up:
	$(COMPOSE) up -d

# build: 
build:
	$(COMPOSE) build --no-cache

# down:
down:
	$(COMPOSE) dowm

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

	