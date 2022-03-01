# Embedded Python Benchmark
This is a repository for SQL benchmarks for Embedded Python. 

Currently, this benchmark compares the sql performance between 
Embedded Python and PostgreSQL. 

## What We Compare

* Inserting data in the dataframe into the database: For Embedded Python, inserts are done by enumerating the dataframe. For PostgreSQL, inserts are done in two ways, 1) by enumerating the dataframe, 2) by dataframe's to_sql() method.

* Reading data into the dataframe: For Embedded Python, the dataframe() method of IRIS result set is used. For PostgreSQL, dataframe's read_sql_query() method is used.

For the to_sql() and read_sql_query() methods, SQLAlchemy is used.

## How To Run
IRIS and PostgreSQL run in separate docker containers. Simply execute:

```
docker-compose up -d
```

to bring up the containers.

After bringing up the containers, run:

```
./run-bench.sh
```

to perform the benchmark.

## Dataset

