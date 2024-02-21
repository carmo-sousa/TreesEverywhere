FROM python:3.12-slim

WORKDIR /app

ARG USERNAME=metatron

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    \
    POETRY_HOME="/app/poetry" \
    VENV_PATH="/app/.venv" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  gcc \
  libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" ${USERNAME} ; pip install poetry

COPY --chown=${USERNAME}:${USERNAME} . .

RUN poetry install

USER ${USERNAME}

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
