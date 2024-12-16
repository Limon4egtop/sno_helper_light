FROM python:3.12-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev cargo

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "main.py"]