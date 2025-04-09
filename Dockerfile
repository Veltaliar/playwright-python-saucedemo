FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN python -m playwright install --with-deps

CMD ["pytest"]
