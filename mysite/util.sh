find . -name "*.pyc" -exec rm -rf {} \;
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser