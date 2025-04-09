FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

# Install fonts, tools, and DM fonts manually
RUN apt-get update && apt-get install -y \
    fonts-liberation \
    fonts-dejavu \
    fonts-noto-cjk \
    fonts-noto-core \
    fonts-noto-ui-core \
    fonts-noto-hinted \
    libfreetype6 fontconfig curl unzip \
    locales \
    --no-install-recommends && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install DM Sans & DM Mono from Google Fonts
RUN mkdir -p /usr/share/fonts/truetype/dm && \
    curl -L -o /tmp/dm-fonts.zip https://github.com/google/fonts/archive/refs/heads/main.zip && \
    unzip -q /tmp/dm-fonts.zip -d /tmp/fonts && \
    cp /tmp/fonts/fonts-main/ofl/dmsans/*.ttf /usr/share/fonts/truetype/dm/ && \
    cp /tmp/fonts/fonts-main/ofl/dmmono/*.ttf /usr/share/fonts/truetype/dm/ && \
    fc-cache -f -v && \
    rm -rf /tmp/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=UTC

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN python -m playwright install --with-deps

CMD ["pytest"]
