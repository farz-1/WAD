# For1 WAD Project Web Application

## Description

Formula One based website that allows users to rate cars, constructors and drivers on a variety of categories.
Also shows some key information about the sport and its schedule.
Users can log in and out of the site and have details about themselves.

### Installing

* You will need to install the following via pip with the commands:
* $ pip install schedule
* $ pip install requests
* $ pip install bcrypt
* We used the NewsAPI for fetching our news stories and bcryptAPI for user authentication. The schedule and requests libraries aid the news API. 

### Setup

* open a terninal and navigate to the project directory
* type "python manage.py makemigrations for1" and hit enter
* type "python manage.py migrate" and hit enter
* run populate_f1.py (the script will continue to run inorder to fetch updated news articles, but you can ternimate it once all the inital data has been imported)
* type "python manage.py runserver" and hit enter
* navigate to the provided URL

## Authors

* Libby Cornwall
* Vaughn Muirhead
* Farzwan Mohamed
* Raphael Nekam
* Joe Lee

## Acknowledgments

Links:
* [requests](https://docs.python-requests.org/en/latest/)
* [schedule](https://schedule.readthedocs.io/en/stable/)
* [bcrypt](https://docs.python-requests.org/en/latest/)
* [NewsAPI](https://newsapi.org/docs/)
