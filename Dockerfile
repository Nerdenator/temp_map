# pull official base image
FROM python:3.8.3-alpine

# set work directory

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc musl-dev postgresql-dev python3-dev

# install dependency
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint
COPY ./entrypoint.sh .

# copy project
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]