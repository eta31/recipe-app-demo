virtualenv -p python3 venv

source venv/bin/activate


python manage.py makemigrations

python manage.py migrate

python manage.py runserver
