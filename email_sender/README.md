# Service Email-Sender

Email Sending Service

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

### Run linters
Installing dependencies from requirements-dev.txt in the project root

```commandline
isort email_sender
flake8 email_sender
black --line-length 120 email_sender
```

### Description of ENV Variables

| Variable Name                           | Possible Value  | Description                                                  |
|:----------------------------------------|-----------------|:-------------------------------------------------------------|
| EMAIL_SENDER_RABBITMQ_SEND_QUEUE_NAME   | email_status    | Name of the queue for sending message delivery statuses      |
| EMAIL_SENDER_RABBITMQ_SOURCE_QUEUE_NAME | emails          | Name of the queue for receiving messages                     |
| SMTP_HOST                               | mailhog         | SMTP server hostname                                         |
| SMTP_PORT                               | 1025            | SMTP server port                                             |
| RABBITMQ_HOST                           | rabbitmq        | RabbitMQ server hostname                                     |
| RABBITMQ_PORT                           | 5672            | RabbitMQ server port                                         |
| RABBITMQ_USER                           | ruser           | RabbitMQ username                                            |
| RABBITMQ_PASS                           | rpassword       | RabbitMQ user password                                       |
| RABBITMQ_VHOST                          |                 | RabbitMQ virtual host name                                   |
| RABBITMQ_EXCHANGE_TYPE                  | topic           | RabbitMQ exchange type                                       |
| RABBITMQ_PREFETCH_COUNT                 | 1               | Number of messages consumed at the same time by the consumer |
