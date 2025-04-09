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

RUN apt-get install -y locales && \
locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=UTC
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN python -m playwright install --with-deps

CMD ["pytest"]
