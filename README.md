# Trees Every

## Tecnologias usadas

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python (3.12.X)](https://www.python.org/)
- [Django (5.X)](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Dynaconf](https://www.dynaconf.com/)

## Configuração do projeto

Recomendo usar o [Poetry](https://python-poetry.org/) com [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) para executar o projeto.

- Clonar o projeto: `git clone https://github.com/carmo-sousa/TreesEverywhere.git`
- Criar um arquivo `.env` na raiz do projeto.

```bash
#--------------------------------------#
# API                                  #
#--------------------------------------#
ENVIRONMENT=development
DJANGO_SETTINGS_MODULE=everywhere.settings

#--------------------------------------#
# DATABASE                             #
#--------------------------------------#
DB_USER=metatron
DB_PASSWORD=12345678
DB_NAME=everywhere
DB_HOST=database
```

- Executar o docker compose: `docker compose --env-file .env up --build -d`
- Aplicar as migrações
  - Com poetry: `poetry run task migrate`
    > Se não tiver o poetry executar o comando: `docker exec api python manage.py migrate`
- Abrir a aplicação: `http://localhost:8080/dashboard`
- Swagger: `http://localhost:8080/api/schema/swagger-ui/`
