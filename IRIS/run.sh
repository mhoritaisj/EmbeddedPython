#!/bin/sh

docker build . -t iris-comm

docker run --name iris-comm -p 53773:1972 -p 54773:52773 -v $(pwd)/../work:/work -d iris-comm