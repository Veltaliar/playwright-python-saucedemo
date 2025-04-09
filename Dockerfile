FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

RUN apt-get update && apt-get install -y \
    fonts-noto-cjk \
    fonts-dejavu-core \
    fonts-dejavu-extra \
    fonts-liberation \
    fonts-freefont-ttf \
    fonts-noto-mono \
    fonts-noto-color-emoji \
    fonts-noto-cjk-extra \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["pytest"]
