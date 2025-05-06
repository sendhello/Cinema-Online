# Admin Panel

Movie Catalog Administration Service

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
# on the root
docker compose up --build
```

## Description of Additional Service Methods

### Running Linters
Installing Dependencies from requirements-dev.txt in the Project Root

```commandline
isort admin_panel
flake8 admin_panel
black --skip-string-normalization admin_panel
```

### Description of ENV Variables

| Variable Name             | Possible Value      | Description        |
|:--------------------------|---------------------|:-------------------|
| DEBUG                     | true                | Debug Mode         |
| DB_HOST                   | localhost           | Host DB            |
| DB_PORT                   | 5434                | Port DB            |
| DB_NAME                   | movies_database     | Name DB            |
| DB_USER                   | app                 | DB Username        |
| DB_PASSWORD               | 123qwe              | DB Password        |
| SECRET_KEY                | secret              | Secret key         |
| ALLOWED_HOSTS             | '*'                 | Allowed Hosts      |
| DJANGO_SUPERUSER_USERNAME | admin               | Superuser name     |
| DJANGO_SUPERUSER_PASSWORD | admin               | Superuser password |
| DJANGO_SUPERUSER_EMAIL    | example@example.com | Superuser Email    |

### Superuser creating
A superuser is created automatically with the login admin and password admin

### External Authentication 
Users of the service are created and verified by the Auth service

### Localization
To create the translation table, run:
```bash
python manage.py makemessages -l en -l ru 
```
Next, you need to edit (add translations to) the .po files in the locale directory.
To apply the translations, compile them using:
```bash
python manage.py compilemessages -l en -l ru 
```
