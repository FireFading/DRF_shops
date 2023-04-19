## features
- get all town from database
- get street in specific town
- create town, shop, street
- get shops in specific town or/and specific street, close/open shops (all params are optional)
> ***

## setup
- - in env.example all variables used in project, change it to .env, several variables that are common, already define as example, secret variables is empty
- in app folder create "media" and "static" folders
- `docker exec -it django python manage.py collectstatic`
- `docker exec -it django python manage.py createsuperuser`

## run
- `docker compose up` OR `make up` - run without building, also you can prove -d flag to run as daemon

## down docker
- `docker compose down && docker network prune --force` OR `make down`

## to test
- `docker exec -it django python manage.py test` OR `make test`

## migrations
- `docker exec -it django python manage.py makemigrations`
- `docker exec -it django python manage.py migrate`
- OR `make migrate`


## formatting and linting
- run ufmt: `ufmt format .`
- run black: `black --config=configs/.black.toml app`
- run ruff: `ruff check --config=configs/.ruff.toml --fix app`
- run flake8: `flake8 --config=configs/.flake8 app`
- OR `nox` in root