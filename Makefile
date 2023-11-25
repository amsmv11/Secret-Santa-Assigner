.PHONY: build clean up stop lint uni-tests integration-tests

make local-build:
	./scripts/local-build.sh

build:
	docker-compose build && \
	docker-compose up -d && \
	docker-compose run --rm webapi alembic upgrade head && \
	docker-compose run --rm pg_db bash -c "echo -e \"log_statement = 'all'\nlog_directory = 'pg_log'\nlog_filename = 'postgres.log'\nlogging_collector = on\nlog_min_error_statement = error\" >> /var/lib/postgresql/data/postgresql.conf" && \
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

migrate:
	docker-compose up -d pg_db && \
	docker-compose run --rm webapi alembic upgrade head && \
	docker-compose run --rm pg_db bash -c "echo -e \"log_statement = 'all'\nlog_directory = 'pg_log'\nlog_filename = 'postgres.log'\nlogging_collector = on\nlog_min_error_statement = error\" >> /var/lib/postgresql/data/postgresql.conf"

unit-tests:
	docker-compose run unit-tests

integration-tests:
	docker-compose run integration-tests
