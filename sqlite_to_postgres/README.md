# Importer

Importer data from sqlite to PostgreSQL

* **Application Language:** Python 3.11
* **Supported Communication Protocols:** None
* **Infrastructure Dependencies:** Postgres
* **System Package Dependencies:** None
* **PostgreSQL Extension Dependencies:** None
* **Environment Role:** development
* **Minimum System Requirements:** 1 CPU, 1Gb RAM

## Service support

Software engineers:

* Ivan Bazhenov (*[@sendhello](https://github.com/sendhello)*)

## Description of Required Methods to Run the Service

### Service Startup
```commandline
on the root
docker compose up --build
```

## Description of Additional Service Methods

### Run linters
Installing dependencies from requirements-dev.txt in the project root

```commandline
isort auth_service
flake8 auth_service
black --skip-string-normalization auth_service
```

### Description of ENV Variables

| Variable Name            | Possible Value                                      | Description                                                             |
|:-------------------------|-----------------------------------------------------|:------------------------------------------------------------------------|
| DEBUG                    | False                                               | Debug mode                                                              |
| PG_DSN                   | postgresql+asyncpg://app:123qwe@localhost:5433/auth | PostgreSQL database DSN (Data Source Name)                              |
