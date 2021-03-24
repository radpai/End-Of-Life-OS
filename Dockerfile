FROM python:3.9.1-alpine

RUN apk update && \
  apk add --no-cache \
    gcc \
    linux-headers \
    musl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    openssl-dev \
    python3-dev \
    python3

RUN pip3 install --upgrade pip
RUN pip3 install scrapy

COPY . .

WORKDIR app/

ENTRYPOINT ["sh", "entrypoint.sh"]
