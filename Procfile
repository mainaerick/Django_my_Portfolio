#Procfile
web: gunicorn Django_Portfolio.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py migrate