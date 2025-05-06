# Сервис Notification Generator

Сервис генерации Нотификаций

* **Application Language:** Python 3.11
* **Supported Communication Protocols:** AMQP
* **Infrastructure Dependencies:** RabbitMQ
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
# on the root
docker compose up --build
```

## Description of Additional Service Methods

### Running linters
Installing dependencies from requirements-dev.txt at the project root

```commandline
isort notification_generator
flake8 notification_generator
black --line-length 120 notification_generator
```

### Description of ENV Variables

| Variable Name                             | Possible Value     | Description                                                  |
|:------------------------------------------|--------------------|:-------------------------------------------------------------|
| NOTIFICATION_API_GATEWAY                  | localhost          | Path to the Notification API service                         |
| REQUEST_PERIOD                            | 30                 | Polling period for the Notification API service (in seconds) |
| AUTH_GATEWAY                              | localhost          | Path to the Auth service                                     |
| ADMIN_EMAIL                               | email_status       | Admin login for the Auth service                             |
| ADMIN_PASSWORD                            | localhost          | Admin password for the Auth service                          |
| NOTIFICATION_GEN_RABBITMQ_SEND_QUEUE_NAME | email_status       | Queue name for sending messages                              |
| RABBITMQ_HOST                             | rabbitmq           | RabbitMQ server name                                         |
| RABBITMQ_PORT                             | 5672               | RabbitMQ server port                                         |
| RABBITMQ_USER                             | ruser              | RabbitMQ username                                            |
| RABBITMQ_PASS                             | rpassword          | RabbitMQ user password                                       |
| RABBITMQ_VHOST                            |                    | RabbitMQ virtual host name                                   |
| RABBITMQ_EXCHANGE_TYPE                    | topic              | RabbitMQ exchange type                                       |
| RABBITMQ_PREFETCH_COUNT                   | 1                  | Number of messages consumed simultaneously by the consumer   |

