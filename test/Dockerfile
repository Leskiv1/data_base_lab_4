FROM python:3.11-slim

WORKDIR /app

COPY test.py .

RUN pip install --no-cache-dir requests

CMD ["python", "test.py"]
