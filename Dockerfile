FROM continuumio/anaconda3:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN conda install -y pandas sqlalchemy psycopg2
