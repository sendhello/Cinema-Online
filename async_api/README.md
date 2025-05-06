# Service Async API

The project provides an asynchronous Web API for searching movie information

* **Application Language:** Python 3.11
* **Supported Communication Protocols:** REST API
* **Infrastructure Dependencies:** Elasticsearch, Redis
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

### Documentation
* http://127.0.0.1/api/api/openapi (Swagger)
* http://127.0.0.1/api/api/openapi.json (openapi)

## Description of Additional Service Methods

### Running functional-tests
```commandline
docker compose -f tests/functional/docker-compose.yml up --build
```

### Description of ENV Variables

| Variable Name     | Possible Value  | Description                        |
|:------------------|-----------------|:-----------------------------------|
| PROJECT_NAME      | Cinema          | Service name (show in the Swagger) |
| ES_HOST           | elasticsearch   | ElasticSearch server name          |
| ES_PORT           | 9200            | ElasticSearch server port          |
| REDIS_HOST        | redis           | Redis server name                  |
| REDIS_PORT        | 6379            | Redis server port                  |
| LOG_LEVEL_LOGGERS | DEBUG           | log level                          |
| LOG_LEVEL_ROOT    | DEBUG           | root log level                     |
