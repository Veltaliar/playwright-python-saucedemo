FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

RUN apt-get update && \
    apt-get install -y fonts-noto-cjk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["pytest"]
