<p align="center">
    <img src="piscuss.png" alt="Piscuss | Opensource Discussion Application">
</p>

<p align="center">
    <a><img src="https://github.com/ethan-v/piscuss/actions/workflows/test-django-app.yml/badge.svg" alt="Build Status"></a>
</p>

Piscuss is a fast and lightweight open source discussion application.

**Technical stack**

- Python 3.8+
- Django 4.x
- Django Rest Framework 3.x

## Features

- [ ] All Threads
- Channels
- Popular This Week
- Popular All Time
- Solved
- Unsolved
- No Replies Yet
- Leaderboard

## Development

Install dependencies with poetry

```shell
poetry shell
poetry install
```

Start project

```shell
python manage.py migrate
python manage.py runserver
```

Create a admin user

```shell
python manage.py createsuperuser
# piscuss / piscuss / piscuss@example.com
```

Run tests

```shell
python manage.py test
```

Check Restful API

```text
http://localhost:8000/api/
```

## Deployment

comming soon...
