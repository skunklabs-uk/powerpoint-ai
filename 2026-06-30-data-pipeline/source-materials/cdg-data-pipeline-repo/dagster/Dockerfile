FROM ghcr.io/astral-sh/uv:0.12.3 AS uv

FROM python:3.12-slim

COPY --from=uv /uv /usr/local/bin/uv

RUN uv pip install --system --no-cache \
    dagster \
    dagster-webserver \
    dagster-mysql \
    dbt-core \
    dbt-mysql \
    "dlt[sqlalchemy]" \
    boto3 \
    openpyxl \
    pandas \
    pymysql \
    pyyaml \
    requests

WORKDIR /opt/dagster/app
ENV DAGSTER_HOME=/opt/dagster/dagster_home

RUN mkdir -p /opt/dagster/dagster_home
