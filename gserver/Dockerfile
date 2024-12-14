FROM python:3.13 AS base
env PIPENV_VENV_IN_PROJECT=1
RUN pip install pipenv
from base as build
COPY . /opt/gserver
WORKDIR /opt/gserver
RUN apt-get update && apt-get install -y build-essential
RUN pipenv install zc.buildout && pipenv run buildout
from base as runtime
COPY --from=build /opt/gserver /opt/gserver
WORKDIR /opt/gserver
ENTRYPOINT ["./start"]
