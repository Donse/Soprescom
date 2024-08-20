python manage.py livereload
python manage.py runserver
celery -A config.celery worker --pool=solo -l info
