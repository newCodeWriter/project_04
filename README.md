# Trade Up

Trade Up is a stock trading application that uses a third party API to retrieve stock data and MySQL and Django for user management and authentication. 

## Contributors

Built and designed by Marshay

## Preview/Demo
<img width="1000" alt="Screen Shot 2021-04-20 at 9 13 12 PM" src="https://user-images.githubusercontent.com/65259996/115483134-32cdd180-a21e-11eb-9441-dc7d816d9993.png">
<img width="1000" alt="Screen Shot 2021-04-20 at 9 14 16 PM" src="https://user-images.githubusercontent.com/65259996/115483137-36615880-a21e-11eb-872e-c9f906bd46dc.png">
<img width="1000" alt="Screen Shot 2021-04-20 at 9 15 57 PM" src="https://user-images.githubusercontent.com/65259996/115483169-44af7480-a21e-11eb-925d-7b2c5b8d3e34.png">
<img width="1000" alt="Screen Shot 2021-04-20 at 9 16 34 PM" src="https://user-images.githubusercontent.com/65259996/115483175-4711ce80-a21e-11eb-95b1-34809118cf58.png">
<img width="1000" alt="Screen Shot 2021-04-20 at 9 13 39 PM" src="https://user-images.githubusercontent.com/65259996/115483664-36158d00-a21f-11eb-8b89-49ec9062adfc.png">


## Tech/Framework

Python <br/>
Django <br/>
Bootstrap <br/>

## Getting started
### Installations (also see readme.txt)

1. Install Django - python -m pip install Django
2. Create project - django-admin startproject appname
3. Create app python manage.py startapp appname
4. Add "appname" to your INSTALLED_APPS setting
5. Include the appname URLconf in your project urls.py
6. Install a database i.e. pipenv install mysqlclient
7. Create admin user - python manage.py createsuperuser
8. Install packages (see pipfile)
9. Instal API key depencies (see below)
10. At root directory, type command pipenv shell
11. Start server - python manage.py runserver

#### Adding API Key Dependencies

This program requires the following API keys. These can be obtained here (follow the instructions on the website links):

- [Yahoo Finance API](https://rapidapi.com/apidojo/api/yahoo-finance1)
- [Morningstar API](https://rapidapi.com/integraatio/api/Morningstar)
- [Twelvedata](https://twelvedata.com/docs#getting-started)

## Features
### Feature Overview

- $1,500 is loaded into the user's account upon signup
- search financial instruments
- view historical data of a selected instrument,
- save financial instruments to a watchlist
- buy and sell shares
- change/reset password
- user can view their trading history

