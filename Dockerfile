FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

# Install fonts, locale, rendering dependencies
RUN apt-get update && apt-get install -y \
    fonts-liberation \
    fonts-dejavu \
    fonts-noto-cjk \
    fonts-noto-core \
    fonts-noto-ui-core \
    fonts-noto-hinted \
    libfreetype6 fontconfig \
    locales \
    --no-install-recommends && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables for consistency
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=UTC

# Copy source code
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install browsers
RUN python -m playwright install --with-deps

# Run tests
CMD ["pytest"]
