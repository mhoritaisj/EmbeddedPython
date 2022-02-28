ARG IMAGE=containers.intersystems.com/intersystems/iris-community-arm64:2021.2.0.651.0
FROM ${IMAGE}

# Time Zone
ENV TZ JST-9

# Language
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
#ENV LC_ALL ja_JP.UTF-8

RUN pip3 install pip --upgrade && pip3 install --target /usr/irissys/mgr/python pandas

WORKDIR /opt/irisapp
#RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisapp
#USER ${ISC_PACKAGE_MGRUSER}

# Copy source files to image
COPY . /opt/irisapp

# load demo stuff
RUN iris start IRIS \
        && iris session IRIS < /opt/irisapp/iris.script && iris stop IRIS quietly
