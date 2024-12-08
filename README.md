# async_pytest

## For DB connection

1. Install [PostgreSQL](https://www.postgresql.org/download/)

You can set your DB host/user/name via `pgAdmin`

2. Install requirements via pip or poetry
```shell
pip install -r requirements.txt
```

```shell
poetry install
```

3. Create `.env` file in project root dir
4. Fill environment variables
```shell
BD_USER=USER_NAME_FOR_BD
BD_PASS=PASSWORD
BD_HOST=HOST_NAME
BD_PORT=HOST_PORT
BD_NAME=NAME_OF_BD
```

5. Run migration script for data population (table creation and data filling)

```shell
alembic upgrade head
```

You can drop table after

```shell
alembic downgrade base
```

## Run tests in `/test` dir

## To Do
1. add endpoints for inserting/deleting users from DB
2. add API docs
3. async tests
4. check all setup ways via requirements and poetry 
