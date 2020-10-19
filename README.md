# Handling Periodic Tasks in Django with Celery, Redis and Docker

Example of how to manage periodic tasks with Django, Celery, and Docker

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-celery-periodic-tasks/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Make sure the message broker `redis` service is running :

```sh
$ docker-compose logs -f 'redis'
```

Open the `django apps` logs service to see if your application is up running:

```sh
$ docker-compose logs -f 'web'
```

Open the logs associated with the `celery-beat` service to see the scheduler running:

```sh
$ docker-compose logs -f 'celery-beat'
```

Open the logs associated with the `celery` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'celery'
```
