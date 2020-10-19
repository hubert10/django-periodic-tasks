# Handling Periodic Tasks in Django with Celery, Redis and Docker

Example of how to manage periodic tasks with Django, Celery, and Docker

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-celery-periodic-tasks/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open the logs associated with the `celery` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'celery'
```

Open the logs associated with the `celery-beat` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'celery-beat'
```

Open the logs associated with the `redis` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'redis'
```

Open the logs associated with the `django apps` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'web'
```
