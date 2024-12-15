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

## Step 5 automated with app startup

5. Run migration script for data population (table creation and data filling)

```shell
alembic upgrade head
```

You can drop table after

```shell
alembic downgrade base
```

## Run application locally

```shell
fastapi dev application/users.py
```

U`ll see output like this with clickable URLs:
```
 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯
```

## Run tests in `/test` dir

## To Do
1. add endpoints for inserting/deleting users from DB
2. ~~add API docs~~
3. async tests with pytest
4. check all setup ways via requirements and poetry 
