# Subscribe Service

Subscription Service

* **Application Language:** Python 3.11
* **Supported Communication Protocols:** REST API
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

### Documentation
* http://127.0.0.1/api/subscribe/openapi (Swagger)
* http://127.0.0.1/api/subscribe/openapi.json (openapi)

## Description of Additional Service Methods

### Running functional-tests
Installing dependencies from requirements-dev.txt at the project root

```commandline
pytest -vv auth_service
```

### Running linters
Installing dependencies from requirements-dev.txt at the project root

```commandline
isort auth_service
flake8 auth_service
black --skip-string-normalization auth_service
```

### Description of ENV Variables

| Variable Name           | Possible Value                 | Description                                |
|:------------------------|--------------------------------|:-------------------------------------------|
| DEBUG                   | False                          | Debug mode                                 |
| PROJECT_NAME            | Auth                           | Name of the service (displayed in Swagger) |
| ENVIRONMENT             | dev                            | Name of the environment                    |
| SHOW_TRACEBACK          | true                           | Show traceback in HTTP response            |
| SUBSCRIBE_POSTGRES_HOST | subscribe-postgres             | Postgres database host                     |
| SUBSCRIBE_POSTGRES_PORT | 5432                           | Postgres database port                     |
| POSTGRES_USER           | app                            | Postgres database username                 |
| POSTGRES_PASSWORD       | 123qwe                         | Postgres user password                     |
| SUBSCRIBE_POSTGRES_DB   | subscribe                      | Postgres database name                     |
| AUTH_GATEWAY            | localhost                      | Path to the Auth service                   |
| YOOKASSA_SHOP_ID        | 123456                         | YooKassa shop ID                           |
| YOOKASSA_API_KEY        | ***                            | YooKassa API key                           |
| YOOKASSA_RETURN_URL     | localhost/path                 | Redirect URL after payment                 |
| SENTRY_DSN              | https://*@*ingest.sentry.io/11 | Sentry DSN address                         |
