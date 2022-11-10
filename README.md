# dbtl
A dbt project written in python for learning purposes. The L stands to Lorena.

## Before use

Make sure postgres is running.

```sh
# using docker
docker run --name pgsql-dev -e POSTGRES_PASSWORD=123456 -p 5432:5432 postgres:15
```

**On windows**

In order to use on power shell, define the following function

```
function dbtl {python app/main.py $args}
```

# TODO

- read from profiles.yml the postgres connection on run.py - ok
- execute each model sql file in run.py
