python -m pip install Django
django-admin startproject project_04 // create project
python manage.py startapp trade_app // create app

Add "trade_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'trade_app',
    ]

Include the trade_app URLconf in your project urls.py like this::

    path('trade_app/', include('trade_app.urls')),

//database setup
pipenv install mysqlclient

//create admin user
python manage.py createsuperuser

pipenv shell
python manage.py runserver
python manage.py shell //interactive python shell
python manage.py makemigrations trade_app // when you made changes to models
python manage.py migrate // create database tables for models