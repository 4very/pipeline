#!/bin/bash

python manage.py livereload &
python manage.py runserver 0.0.0.0:8000 &
wait -n
exit $?