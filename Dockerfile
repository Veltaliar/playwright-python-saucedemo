FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["pytest"]