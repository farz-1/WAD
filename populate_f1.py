import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')

import django
django.setup()

from f1.models import Driver, Constructor, Car, Race
import news_api


def populate():
    # 1.0 pictures???
    # 2.0 adding ratings funcs like add_driver rating.
    # 3.0 car categories unable to find.

    driver_list = [
        {'name': 'Lewis Hamilton', 'DOB': '07/01/1985', 'picture': '', 'height': '1.74m', 'weight': '73kg',
         'nationality': 'British', 'driverNumber': 44, 'seasonsWon': 7, 'podiumsWon': 182,'constructor':'Mercedes AMG Petronas F1 Team'},
        {'name': 'George Russell', 'DOB': '15/02/1998', 'picture': '', 'height': '1.85m', 'weight': '70kg',
         'nationality': 'British', 'driverNumber': 63, 'seasonsWon': 0, 'podiumsWon': 1,'constructor':'Mercedes AMG Petronas F1 Team'},
        {'name': 'Max Verstappen', 'DOB': '30/09/1997', 'picture': '', 'height': '1.81m', 'weight': '72kg',
         'nationality': 'Belgian-Dutch', 'driverNumber': '1', 'seasonsWon': 1, 'podiumsWon': 60,'constructor':'Oracle Red Bull Racing'},
        {'name': 'Sergio Perez', 'DOB': '26/01/1990', 'picture': '', 'height': '1.73m', 'weight': '63kg',
         'nationality': 'Mexican', 'driverNumber': 11, 'seasonsWon': 0, 'podiumsWon': 15,'constructor':'Oracle Red Bull Racing'},
        {'name': 'Lando Norris', 'DOB': '13/11/1999', 'picture': '', 'height': '1.7m', 'weight': '66kg',
         'nationality': 'British', 'driverNumber': 4, 'seasonsWon': 0, 'podiumsWon': 5, 'constructor':'McLaren F1 Team'},
        {'name': 'Daniel Ricciardo', 'DOB': '01/07/1989', 'picture': '', 'height': '1.8m', 'weight': '72kg',
         'nationality': 'Australian', 'driverNumber': 3, 'seasonsWon': 0, 'podiumsWon': 32,'constructor':'McLaren F1 Team'},
        {'name': 'Carlos Sainz', 'DOB': '01/09/1994', 'picture': '', 'height': '1.78m', 'weight': '64kg',
         'nationality': 'Spanish', 'driverNumber': 3, 'seasonsWon': 0, 'podiumsWon': 6,'constructor':'Scuderia Ferrari'},
        {'name': 'Charles Leclerc', 'DOB': '16/10/1997', 'picture': '', 'height': '1.8m', 'weight': '69kg',
         'nationality': 'Monocan', 'driverNumber': 16, 'seasonsWon': 0, 'podiumsWon': 13,'constructor':'Scuderia Ferrari'},
        {'name': 'Fernando Alonso', 'DOB': '29/07/1981', 'picture': '', 'height': '1.71m', 'weight': '68kg',
         'nationality': 'Spanish', 'driverNumber': 14, 'seasonsWon': 2, 'podiumsWon': 98,'constructor':'Alpine F1 Team'},
        {'name': 'Esteban Ocon', 'DOB': '17/09/1996', 'picture': '', 'height': '1.86m', 'weight': '66kg',
         'nationality': 'French', 'driverNumber': 31, 'seasonsWon': 0, 'podiumsWon': 2,'constructor':'Alpine F1 Team'},
        {'name': 'Pierre Gasly', 'DOB': '07/02/1996', 'picture': '', 'height': '1.77m', 'weight': '70kg',
         'nationality': 'French', 'driverNumber': 10, 'seasonsWon': 0, 'podiumsWon': 3,'constructor':'Scuderia AlphaTauri'},
        {'name': 'Yuki Tsunoda', 'DOB': '11/05/2000', 'picture': '', 'height': '1.59m', 'weight': '54kg',
         'nationality': 'Japanese', 'driverNumber': 22, 'seasonsWon': 0, 'podiumsWon': 0,'constructor':'Scuderia AlphaTauri'},
        {'name': 'Sebastian Vettel', 'DOB': '3/07/1987', 'picture': '', 'height': '1.75m', 'weight': '62kg',
         'nationality': 'German', 'driverNumber': 5, 'seasonsWon': 4, 'podiumsWon': 122,'constructor':'Aston Martin Aramco Cognizant F1 Team'},
        {'name': 'Lance Stroll', 'DOB': '29/10/1998', 'picture': '', 'height': '1.82m', 'weight': '70kg',
         'nationality': 'Canadian', 'driverNumber': 18, 'seasonsWon': 0, 'podiumsWon': 3, 'constructor':'Aston Martin Aramco Cognizant F1 Team'},
        {'name': 'Alexander Albon', 'DOB': '23/03/1996', 'picture': '', 'height': '1.86m', 'weight': '73kg',
         'nationality': 'Thai', 'driverNumber': 23, 'seasonsWon': 0, 'podiumsWon': 2,'constructor':'Williams Racing'},
        {'name': 'Nicholas Latifi', 'DOB': '29/07/1995', 'picture': '', 'height': '1.85m', 'weight': '73kg',
         'nationality': 'Canadian', 'driverNumber': 6, 'seasonsWon': 0, 'podiumsWon': 0,'constructor':'Williams Racing'},
        {'name': 'Mick Schumacher', 'DOB': '22/03/1999', 'picture': '', 'height': '1.77m', 'weight': '67kg',
         'nationality': 'German', 'driverNumber': 47, 'seasonsWon': 0, 'podiumsWon': 0,'constructor':'Haas F1 Team'},
        {'name':'Kevin Magnussen','DOB': '05/10/1992', 'picture': '', 'height': '1.74m', 'weight': '68kg',
         'nationality': 'Danish', 'driverNumber': 20, 'seasonsWon': 0, 'podiumsWon': 1,'constructor':'Haas F1 Team'},
        {'name': 'Valtteri Bottas', 'DOB': '28/08/1989', 'picture': '', 'height': '1.73m', 'weight': '69kg',
         'nationality': 'Finnish', 'driverNumber': 77, 'seasonsWon': 0, 'podiumsWon': 67,'constructor':'Alfa Romeo F1 Team Orlen'},
        {'name': 'Guanyu Zhou', 'DOB': '30/05/1999', 'picture': '', 'height': '1.75m',
         'weight': '63kg', 'nationality': 'Chinese', 'driverNumber': 24, 'seasonsWon': 0, 'podiumsWon': 0,'constructor':'Alfa Romeo F1 Team Orlen'}]

    constructor_list = [
        {'name': 'Mercedes AMG Petronas F1 Team', 'teamPrincipal': 'Totto Wolff', 'nationality': 'German',
         'yearsActive': 68, 'raceEngineer': 'Peter Bonnington'},
        {'name': 'Oracle Red Bull Racing', 'teamPrincipal': 'Christian Horner', 'nationality': 'Austrian',
         'yearsActive': 17, 'raceEngineer': 'Gianpiero Lambiase'},
        {'name': 'McLaren F1 Team', 'teamPrincipal': 'Zak Brown', 'nationality': 'British',
         'yearsActive': 56, 'raceEngineer': 'William Joseph'},
        {'name': 'Scuderia Ferrari', 'teamPrincipal': 'Mattia Binotto', 'nationality': 'Italian',
         'yearsActive': 72, 'raceEngineer': 'Riccardo Adami'},
        {'name': 'Alpine F1 Team', 'teamPrincipal': 'Otmar Szafnauer', 'nationality': 'French', 'yearsActive': 1,
         'raceEngineer': 'Karel Loos'},
        {'name': 'Scuderia AlphaTauri', 'teamPrincipal': 'Franz Tost', 'nationality': 'Italian', 'yearsActive': 18,
         'raceEngineer': 'Pierre Hamelin'},
        {'name': 'Aston Martin Aramco Cognizant F1 Team', 'teamPrincipal': 'Lawrence Stroll', 'nationality': 'British',
         'yearsActive': 63, 'raceEngineer': 'Ben Michell'},
        {'name': 'Williams Racing', 'teamPrincipal': 'Jost Capito', 'nationality': 'British', 'yearsActive': 44,
         'raceEngineer': 'Paul Williams'},
        {'name': 'Haas F1 Team', 'teamPrincipal': 'Guenther Steiner', 'nationality': 'American', 'yearsActive': 8,
         'raceEngineer': 'Ayao Komatsu'},
        {'name': 'Alfa Romeo F1 Team Orlen', 'teamPrincipal': 'Frédéric Vasseur', 'nationality': 'Italian',
         'yearsActive': 72, 'raceEngineer': 'Ruth Buscombe'}]

    car_list = [{'model': 'Mercedes-AMG F1 W12 E Performance', 'horsepower': '', 'engineSupplier': '', 'picture': '', 'gearbox': ''}]

    race_list = [
        {'location': 'Bahrain - Sakhir', 'trackLength': '5.412km', 'date': '18-20/03/2022', 'laps': 57,
         'time': '15:00-17:00'},
        {'location': 'Saudi Arabia - Jeddah', 'trackLength': '6.174km', 'date': '25-27/03/2022', 'laps': 50,
         'time': '18:00-20:00'},
        {'location': 'Australia - Melbourne', 'trackLength': '5.303km', 'date': '08-10/04/2022', 'laps': 58,
         'time': '06:00-08:00'},
        {'location': 'Italy - Imola', 'trackLength': '5.793km', 'date': '22-24/04/2022', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'United States - Miami', 'trackLength': '5.410km', 'date': '06-08/05/2022', 'laps': 57,
         'time': '08:30-22:30'},
        {'location': 'Spain - Catalunya', 'trackLength': '4.655km', 'date': '20-22/05/2022', 'laps': 66,
         'time': '14:00-16:00'},
        {'location': 'Monaco - Monaco', 'trackLength': '3.337km', 'date': '27-29/05/2022', 'laps': 78,
         'time': '14:00-16:00'},
        {'location': 'Azerbaijan - Baku', 'trackLength': '6.003km', 'date': '10-12/06/2022', 'laps': 51,
         'time': '12:00-14:00'},
        {'location': 'Canada - Montreal', 'trackLength': '4.361km', 'date': '17-19/06/2022', 'laps': 70,
         'time': '19:00-21:00'},
        {'location': 'Great Britain - Baku', 'trackLength': '6.003km', 'date': '10-12/06/2022', 'laps': 51,
         'time': '12:00-14:00'},
        {'location': 'Great Britain - Silverstone', 'trackLength': '5.891km', 'date': '01-03/07/2022',
         'laps': 52, 'time': '15:00-17:00'},
        {'location': 'Austria - Spielberg', 'trackLength': '	4.318km', 'date': '10-tbc/07/2022', 'laps': 71,
         'time': '14:00-16:00'},
        {'location': 'France - Le Castellet', 'trackLength': '5.842km', 'date': '22-24/07/2022', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'Hungary - Mogyoród', 'trackLength': '4.381km', 'date': '29-31/07/2022', 'laps': 70,
         'time': '14:00-16:00'},
        {'location': 'Belgium - Spa', 'trackLength': '7.004km', 'date': '26-28/08/2022', 'laps': 44,
         'time': '14:00-16:00'},
        {'location': 'Netherlands - Zandvoort', 'trackLength': '4.259km', 'date': '02-04/09/2022', 'laps': 72,
         'time': '14:00-16:00'},
        {'location': 'Italy - Monza', 'trackLength': '5.793km', 'date': '09-11/09/2022', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'Singapore - Marina Bay', 'trackLength': '5.063km', 'date': '30-02/09-10/2022',
         'laps': 61, 'time': '13:00-15:00'},
        {'location': 'Japan - Suzuka', 'trackLength': '5.807km', 'date': '07-09/10/2022', 'laps': 53,
         'time': '06:00-08:00'},
        {'location': 'United States - Austin', 'trackLength': '5.513km', 'date': '21-23/10/2022', 'laps': 56,
         'time': '20:00-22:00'},
        {'location': 'Mexico - Mexico City', 'trackLength': '4.304km', 'date': '28-30/10/2022', 'laps': 71,
         'time': '20:00-22:00'},
        {'location': 'Brazi - São Paulo', 'trackLength': '4.309km', 'date': '11-13/11/2022', 'laps': 71,
         'time': '20:00-22:00'},
        {'location': 'Abu Dhabi - United Arab Emirates', 'trackLength': '5.554km', 'date': '18-20/11/2022', 'laps': 55,
         'time': '13:00-15:00'}]

    for i in driver_list:
        add_driver(i['name'], i['DOB'], i['picture'], i['height'], i['weight'], i['nationality'], i['driverNumber'],
                   i['seasonsWon'], i['podiumsWon'])

    for i in constructor_list:
        add_constructor(i['name'], i['teamPrincipal'], i['nationality'], i['yearsActive'], i['raceEngineer'])

    for i in car_list:
        add_car(i['model'], i['horsepower'], i['engineSupplier'], i['picture'], i['gearbox'])

    for i in race_list:
        add_race(i['location'], i['trackLength'], i['date'], i['laps'], i['time'])


def add_driver(name, DOB, picture, height, weight, nationality, driverNum, seasonsWon, podiumsWon):
    record = Driver.objects.get_or_create(name=name, DOB=DOB, picture=picture, height=height, weight=weight,
                                          nationality=nationality, driverNumber=driverNum, seasonsWon=seasonsWon,
                                          podiumsWon=podiumsWon)[0]
    record.save()
    print("Driver record \"" + name + "\" added.")


def add_constructor(name, teamPrincipal, nationality, yearsActive, raceEngineer):
    record = Constructor.objects.get_or_create(name=name, teamPrincipal=teamPrincipal, nationality=nationality,
                                               yearsActive=yearsActive, raceEngineer=raceEngineer)[0]
    record.save()
    print("Constructor record \"" + name + "\" added.")


def add_car(model, horsepower, engineSupplier, picture, gearbox):
    record = Car.objects.get_or_create(model=model, horsepower=horsepower, engineSupplier=engineSupplier,
                                       picture=picture, gearbox=gearbox)[0]
    record.save()
    print("Car record \"" + model + "\" added.")


def add_race(location, trackLength, date, laps, time):
    record = Race.objects.get_or_create(location=location, trackLength=trackLength, date=date, laps=laps, time=time)[0]
    record.save()
    print("Race record \"" + location + "\" added.")


populate()
news_api.get_news()  # ensures database is populated before running timed calls
print("Database Populated! This script will continue to run fetching updated news every hour.")
news_api.run()
