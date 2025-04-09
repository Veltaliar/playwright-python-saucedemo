FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

RUN apt-get update && apt-get install -y \
    fonts-liberation \
    fonts-dejavu \
    fonts-noto-cjk \
    fonts-noto-core \
    fonts-noto-ui-core \
    fonts-noto-hinted \
    libfreetype6 fontconfig curl unzip \
    --no-install-recommends && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download and install DM Mono and DM Sans
RUN mkdir -p /usr/share/fonts/truetype/dm && \
    curl -L -o /tmp/dm-fonts.zip https://github.com/google/fonts/archive/refs/heads/main.zip && \
    unzip -q /tmp/dm-fonts.zip -d /tmp/fonts && \
    cp /tmp/fonts/fonts-main/ofl/dmsans/*.ttf /usr/share/fonts/truetype/dm/ && \
    cp /tmp/fonts/fonts-main/ofl/dmmono/*.ttf /usr/share/fonts/truetype/dm/ && \
    fc-cache -f -v && \
    rm -rf /tmp/*

# Copy source code
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Run tests
CMD ["pytest"]
