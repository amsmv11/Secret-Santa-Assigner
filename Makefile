.PHONY: build clean up stop lint uni-tests integration-tests

build:
	docker-compose build && \
	docker-compose up -d && \
	docker-compose stop

clean:
	docker-compose down --volumes --remove-orphans --rmi local && \
	docker image prune -f

up:
	docker-compose up -d

stop:
	docker-compose stop

lint:
	./scripts/lint.sh

migration:
	docker-compose up -d pg_db && \
	docker-compose run --rm webapi alembic revision --autogenerate -m "${MESSAGE}" && \
	docker-compose down

unit-tests:
	docker-compose run unit-tests

integration-tests:
	docker-compose run integration-tests
