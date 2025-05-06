# Notification API Service

Notification Service

* **Application Language:** Python 3.11
* **Supported Communication Protocols:** REST API, AMQP
* **Infrastructure Dependencies:** Postgres, RabbitMQ
* **System Package Dependencies:** None
* **PostgreSQL Extension Dependencies:** None
* **Environment Part:** development
* **Minimum System Requirements:** 1 CPU, 1Gb RAM

## Service Support

Development Team:

* Ivan Bazhenov (@sendhello)

## Required Methods for Starting the Service

### Starting the Service
```commandline
# From the project root
docker compose up --build
```

### Documentation
* http://127.0.0.1/api/notification/openapi (Swagger)
* http://127.0.0.1/api/notification/openapi.json (OpenAPI)

## Description of Additional Service Methods

### Running Linters
Install dependencies from requirements-dev.txt at the project root

```commandline
isort notification_api
flake8 notification_api
black --line-length 120 notification_api
```

### Description of ENV Variables

| Variable Name                            | Possible Value    | Description                                                |
|:-----------------------------------------|-------------------|:-----------------------------------------------------------|
| PROJECT_NAME                             | Notification API  | Service name (displayed in Swagger)                        |
| POSTGRES_USER                            | app               | Postgres username                                          |
| POSTGRES_PASSWORD                        | 123qwe            | Postgres user password                                     |
| NOTIFICATION_POSTGRES_DB                 | notification_db   | Name of the Postgres database                              |
| AUTH_GATEWAY                             | localhost         | Path to Auth service                                       |
| NOTIFICATIONS_TASK_BACKOFF_MAX_TIME      | email_status      | Backoff wait time                                          |
| NOTIFICATIONS_POSTGRES_HOST              | localhost         | Postgres server address                                    |
| NOTIFICATIONS_POSTGRES_PORT              | 5432              | Postgres server port                                       |
| NOTIFICATIONS_RABBITMQ_SOURCE_QUEUE_NAME | email_status      | Queue name for receiving message delivery statuses         |
| RABBITMQ_HOST                            | rabbitmq          | RabbitMQ server name                                       |
| RABBITMQ_PORT                            | 5672              | RabbitMQ server port                                       |
| RABBITMQ_USER                            | ruser             | RabbitMQ username                                          |
| RABBITMQ_PASS                            | rpassword         | RabbitMQ user password                                     |
| RABBITMQ_VHOST                           |                   | RabbitMQ virtual host name                                 |
| RABBITMQ_EXCHANGE_TYPE                   | topic             | RabbitMQ exchange type                                     |
| RABBITMQ_PREFETCH_COUNT                  | 1                 | Number of messages consumed simultaneously by the consumer |
