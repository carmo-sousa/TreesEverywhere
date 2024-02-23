# Trees Every

## Tecnologias usadas

- Docker
- Docker compose
- Python (3.12.X)
- Django (5.X)
- Django RestFramework

## Configuração do projeto

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
- Abrir a aplicação: `http://localhost:8080/dashboard`
- Swagger: `http://localhost:8080/api/schema/swagger-ui/`
