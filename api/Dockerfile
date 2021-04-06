FROM python:3

RUN mkdir -p /usr/src/app \
    && apt-get -y update \
    && apt-get install -y supervisor \
    && pip install -U pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
