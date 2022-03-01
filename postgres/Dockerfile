FROM arm64v8/postgres:14-alpine

# Time Zone
ENV TZ Asia/Tokyo

# Language
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

RUN apk --update-cache add python3 python3-dev py3-pip gcc musl-dev \
    && apk add py3-numpy py3-pandas py3-sqlalchemy
RUN pip3 install pip setuptools wheel --upgrade && pip3 install psycopg2

COPY sql/*.sql /docker-entrypoint-initdb.d/
