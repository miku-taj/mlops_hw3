FROM python:3.12.1-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry==2.2.1

# установка зависимостей
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi --only main

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8008"]
