FROM python:3.9.16-alpine

RUN apk add --update \
    tzdata

RUN cd /usr/share/zoneinfo
RUN cp /usr/share/zoneinfo/America/Bogota /etc/localtime

# set work directory
WORKDIR /usr/src/ARSAC

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/ARSAC/entrypoint.sh"]