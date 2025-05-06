# Online-cinema

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
