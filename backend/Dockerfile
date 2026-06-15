# FROM python:3.13-alpine

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ .
# EXPOSE 80

# CMD ["python", "app.py"]

FROM python:3.13-slim

WORKDIR /app

# Устанавливаем системные зависимости (для psycopg2)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код бэкенда
COPY . .

# Переменные окружения (могут быть переопределены в compose)
ENV PYTHONPATH=/app

# Команда для запуска FastAPI (через uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
