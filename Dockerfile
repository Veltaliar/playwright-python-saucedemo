FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN python -m playwright install --with-deps

RUN addgroup --gid 1001 runner && \
    adduser --disabled-password --gecos '' --uid 1001 --gid 1001 runner && \
    chown -R runner:runner /app

RUN mkdir -p /app/test_results
