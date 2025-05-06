# Subscribe Controller

Subscription Automation Service

* **Application Language:** Python 3.11
* **Supported Communication Protocols:** REST API
* **Infrastructure Dependencies:** None
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

### Running linters
Installing dependencies from requirements-dev.txt at the project root

```commandline
isort auth_service
flake8 auth_service
black --skip-string-normalization auth_service
```

### Description of ENV Variables

| Variable Name                    | Possible Value                       | Description                                                  |
|:---------------------------------|--------------------------------------|:-------------------------------------------------------------|
| ENVIRONMENT                      | dev                                  | Name of the environment                                      |
| DEBUG                            | true                                 | Debug mode                                                   |
| SUBSCRIBE_SERVICE_GATEWAY        | localhost                            | Path to the Subscribe Service                                |
| NOTIFICATION_API_GATEWAY         | localhost                            | Path to the Notification API service                         |
| AUTH_GATEWAY                     | localhost                            | Path to the Auth service                                     |
| ADMIN_EMAIL                      | admin@example.com                    | Admin login for the Auth service                             |
| ADMIN_PASSWORD                   | ***                                  | Admin password for the Auth service                          |
| SUBSCRIBE_ROLE_ID                | 482ebcaf-47ec-4ba2-a47b-8e930867d56f | ID of the subscriber role in the Auth service                |
| NOTIFY_DAYS_BEFORE_END_SUBSCRIBE | 2                                    | How many days in advance to notify about subscription expiry |
