# pull official base image
ARG BASE_IMAGE=python:3.8.3-slim-buster

FROM ${BASE_IMAGE} AS compile-image


# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc cron \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv pytest
COPY Pipfile* ./
RUN pipenv lock -r > requirements.txt

# add app
FROM ${BASE_IMAGE} AS runtime-image
WORKDIR /usr/src/app
COPY --from=compile-image /usr/src/app/requirements.txt /usr/src/app/requirements.txt

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc cron \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80

# run entrypoint.sh for wait a conainer
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
