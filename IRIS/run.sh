#!/bin/sh

ARCH=`uname -m`
echo $ARCH
if [ ${ARCH} = 'aarch64' ] || [ ${ARCH} = 'arm64' ]; then
    IMAGE=containers.intersystems.com/intersystems/iris-community-arm64:2021.2.0.651.0
else
    IMAGE=containers.intersystems.com/intersystems/iris-community:2021.2.0.651.0
fi

docker build --build-arg IMAGE=${IMAGE} . -t iris-comm

docker run --name iris-comm -p 53773:1972 -p 54773:52773 -v $(pwd)/../work:/work -d iris-comm