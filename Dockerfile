FROM python

RUN apt-get -y update && \
    apt-get install -y libgl1-mesa-glx poppler-utils


ARG APP_ENVIRONMENT=development

RUN groupadd -r app &&\
    useradd -r -g app -d /home/app -s /sbin/nologin -c "Docker image user" app

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.4.2 \
    APP_PORT=8000 \
    APP_ENVIRONMENT=${APP_ENVIRONMENT}

RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /secret_santa
COPY poetry.lock pyproject.toml /secret_santa/

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi

COPY . /secret_santa

RUN chown -R app:app /secret_santa && chmod 777 /secret_santa

USER app

EXPOSE ${APP_PORT}
