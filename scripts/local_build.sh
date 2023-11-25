#!/usr/bin/env sh
set -ex

export DATABASE_URL="postgresql://postgres:postgres@localhost:5439/secret_santa_db"

###
# some more env variables

# MAIL_PASSWORD=
# EMAIL_ADDRESS=
###

make clean

docker compose -f docker-compose-local.yml up

poetry run alembic upgrade head

poetry run uvicorn main:create_app --reload --host 0.0.0.0 --port 8000