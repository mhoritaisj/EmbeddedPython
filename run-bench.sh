#!/bin/bash

echo 'Running queries for IRIS...'
docker exec -it iris-comm-py /usr/irissys/bin/irispython /work/bench-iris.py

echo ''

echo 'Running queries for PostgreSQL'
docker exec -it postgres-py python3 /work/bench.py