#!/bin/bash

pipenv run python manage.py livereload &
pipenv run python manage.py runserver 0.0.0.0:8000 &
wait -n
exit $?