#!/bin/sh

docker build . -t postgres-py

docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -v $(pwd)/../work:/work -d postgres-py