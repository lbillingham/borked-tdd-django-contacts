# django-contacts
Simple addressbook app using django.
Demo for use with `django` `runserver`,
not a deployment ready project.

## Features

- list organisations and people
- allow the user to see the names and contact details of people in organisations
- user can manage the people who are in an organisation.
- each organisation should have a name and contact details
- organisations and people can be created, edited and deleted.

## Setup
assuming a `python` environment
with

```shell
$ python --version
3.5.2
```
then

```shell
$ pip install requirements_dev.txt
```
## Usage
from the folder containg `manage.py` run

```shell
$ python manage.py runserver
```
and point a browser at `http://localhost:8000/`
