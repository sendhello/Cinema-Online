# Online-cinema

Online Cinema Platform - Subscription-Based Streaming Service
A robust backend system for a subscription-based online cinema platform, featuring comprehensive content management, secure authentication, and automated billing processes.

### Functionality and Features:

* Administration of the movie and genre catalog by the manager
* Importing the catalog from SQLite
* ETL process for migrating the catalog to Elasticsearch
* API for catalog management with fast search and filtering
* Client account (personal cabinet) with Google account authentication
* Subscription system with automatic termination/renewal
* Billing system (Yandex Kassa)
* Payment gateway integration
* Email notifications
* Logging in Kibana and request tracing in Jagger
* Extensibility (adding payment gateways, notification types)
* The system is capable of handling high loads

### Services list:
* [Admin Panel](admin_panel/README.md)
* [SQLite to Postgres](sqlite_to_postgres/README.md)
* [ETL](etl/README.md)
* [Async API](async_api/README.md)
* [Auth](auth_service/README.md)
* [Email Sender](email_sender/README.md)
* [Notification API](notification_api/README.md)
* [Notification Generator](notification_generator/README.md)
* [Subscribe Service](subscribe_service/README.md)
* [Subscribe Controller](subscribe_controller/README.md)

### Project support

Engineers:

* Иван Баженов (*[@sendhello](https://github.com/sendhello)*)

### Run services
```commandline
docker compose up --build
```

### Jaeger-trace
http://localhost:16686

### Run functional-tests

##### Service Async-API
```commandline
docker compose -f tests/functional/docker-compose.yml up --build
```

##### Service Auth
```commandline
pytest -vv auth_service
```
