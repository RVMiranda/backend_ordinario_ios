FROM python:3.11

# Evitar buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Asegurar que el entrypoint sea ejecutable
RUN chmod +x docker/entrypoint.sh || true

CMD ["sh", "/app/docker/entrypoint.sh"]
