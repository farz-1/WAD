import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')

import django
django.setup()

from f1.models import *
import news_api


def populate():
    # 1.0 picture thing
    # 2.0 user updates (vaughn) /  password with raph


    driver_list = [
        {'name': 'Lewis Hamilton', 'DOB': '07/01/1985', 'height': '1.74m', 'weight': '73kg',
         'nationality': 'British', 'driverNumber': 44, 'seasonsWon': 7, 'podiumsWon': 182,
         'constructor': 'Mercedes'},
        {'name': 'George Russell', 'DOB': '15/02/1998', 'height': '1.85m', 'weight': '70kg',
         'nationality': 'British', 'driverNumber': 63, 'seasonsWon': 0, 'podiumsWon': 1,
         'constructor': 'Mercedes'},
        {'name': 'Max Verstappen', 'DOB': '30/09/1997', 'height': '1.81m', 'weight': '72kg',
         'nationality': 'Belgian-Dutch', 'driverNumber': '1', 'seasonsWon': 1, 'podiumsWon': 60,
         'constructor': 'Red Bull'},
        {'name': 'Sergio Perez', 'DOB': '26/01/1990', 'height': '1.73m', 'weight': '63kg',
         'nationality': 'Mexican', 'driverNumber': 11, 'seasonsWon': 0, 'podiumsWon': 15,
         'constructor': 'Red Bull'},
        {'name': 'Lando Norris', 'DOB': '13/11/1999', 'height': '1.7m', 'weight': '66kg',
         'nationality': 'British', 'driverNumber': 4, 'seasonsWon': 0, 'podiumsWon': 5,
         'constructor': 'McLaren'},
        {'name': 'Daniel Ricciardo', 'DOB': '01/07/1989', 'height': '1.8m', 'weight': '72kg',
         'nationality': 'Australian', 'driverNumber': 3, 'seasonsWon': 0, 'podiumsWon': 32,
         'constructor': 'McLaren'},
        {'name': 'Carlos Sainz', 'DOB': '01/09/1994', 'height': '1.78m', 'weight': '64kg',
         'nationality': 'Spanish', 'driverNumber': 3, 'seasonsWon': 0, 'podiumsWon': 6,
         'constructor': 'Ferrari'},
        {'name': 'Charles Leclerc', 'DOB': '16/10/1997', 'height': '1.8m', 'weight': '69kg',
         'nationality': 'Monocan', 'driverNumber': 16, 'seasonsWon': 0, 'podiumsWon': 13,
         'constructor': 'Ferrari'},
        {'name': 'Fernando Alonso', 'DOB': '29/07/1981', 'height': '1.71m', 'weight': '68kg',
         'nationality': 'Spanish', 'driverNumber': 14, 'seasonsWon': 2, 'podiumsWon': 98,
         'constructor': 'Alpine'},
        {'name': 'Esteban Ocon', 'DOB': '17/09/1996', 'height': '1.86m', 'weight': '66kg',
         'nationality': 'French', 'driverNumber': 31, 'seasonsWon': 0, 'podiumsWon': 2,
         'constructor': 'Alpine'},
        {'name': 'Pierre Gasly', 'DOB': '07/02/1996', 'height': '1.77m', 'weight': '70kg',
         'nationality': 'French', 'driverNumber': 10, 'seasonsWon': 0, 'podiumsWon': 3,
         'constructor': 'AlphaTauri'},
        {'name': 'Yuki Tsunoda', 'DOB': '11/05/2000', 'height': '1.59m', 'weight': '54kg',
         'nationality': 'Japanese', 'driverNumber': 22, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'AlphaTauri'},
        {'name': 'Sebastian Vettel', 'DOB': '3/07/1987', 'height': '1.75m', 'weight': '62kg',
         'nationality': 'German', 'driverNumber': 5, 'seasonsWon': 4, 'podiumsWon': 122,
         'constructor': 'Aston Martin'},
        {'name': 'Lance Stroll', 'DOB': '29/10/1998', 'height': '1.82m', 'weight': '70kg',
         'nationality': 'Canadian', 'driverNumber': 18, 'seasonsWon': 0, 'podiumsWon': 3,
         'constructor': 'Aston Martin'},
        {'name': 'Alexander Albon', 'DOB': '23/03/1996', 'height': '1.86m', 'weight': '73kg',
         'nationality': 'Thai', 'driverNumber': 23, 'seasonsWon': 0, 'podiumsWon': 2, 
         'constructor': 'Williams'},
        {'name': 'Nicholas Latifi', 'DOB': '29/07/1995', 'height': '1.85m', 'weight': '73kg',
         'nationality': 'Canadian', 'driverNumber': 6, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Williams'},
        {'name': 'Mick Schumacher', 'DOB': '22/03/1999', 'height': '1.77m', 'weight': '67kg',
         'nationality': 'German', 'driverNumber': 47, 'seasonsWon': 0, 'podiumsWon': 0, 
         'constructor': 'Haas'},
        {'name': 'Kevin Magnussen', 'DOB': '05/10/1992', 'height': '1.74m', 'weight': '68kg',
         'nationality': 'Danish', 'driverNumber': 20, 'seasonsWon': 0, 'podiumsWon': 1, 
         'constructor': 'Haas'},
        {'name': 'Valtteri Bottas', 'DOB': '28/08/1989', 'height': '1.73m', 'weight': '69kg',
         'nationality': 'Finnish', 'driverNumber': 77, 'seasonsWon': 0, 'podiumsWon': 67,
         'constructor': 'Alfa Romeo'},
        {'name': 'Guanyu Zhou', 'DOB': '30/05/1999', 'height': '1.75m',
         'weight': '63kg', 'nationality': 'Chinese', 'driverNumber': 24, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Alfa Romeo'},
        {'name': 'Nico Hulkenberg', 'DOB': '19/08/1987', 'height': '1.84m',
         'weight': '78kg', 'nationality': 'German', 'driverNumber': 27, 'seasonsWon': 0, 'podiumsWon': 0,
         'constructor': 'Aston Martin'}]

    constructor_list = [
        {'name': 'Mercedes', 'teamPrincipal': 'Totto Wolff', 'nationality': 'German',
         'yearsActive': 68, 'raceEngineer': 'Peter Bonnington'},
        {'name': 'Red Bull', 'teamPrincipal': 'Christian Horner', 'nationality': 'Austrian',
         'yearsActive': 17, 'raceEngineer': 'Gianpiero Lambiase'},
        {'name': 'McLaren', 'teamPrincipal': 'Zak Brown', 'nationality': 'British',
         'yearsActive': 56, 'raceEngineer': 'William Joseph'},
        {'name': 'Ferrari', 'teamPrincipal': 'Mattia Binotto', 'nationality': 'Italian',
         'yearsActive': 72, 'raceEngineer': 'Riccardo Adami'},
        {'name': 'Alpine', 'teamPrincipal': 'Otmar Szafnauer', 'nationality': 'French', 'yearsActive': 1,
         'raceEngineer': 'Karel Loos'},
        {'name': 'AlphaTauri', 'teamPrincipal': 'Franz Tost', 'nationality': 'Italian', 'yearsActive': 18,
         'raceEngineer': 'Pierre Hamelin'},
        {'name': 'Aston Martin', 'teamPrincipal': 'Lawrence Stroll', 'nationality': 'British',
         'yearsActive': 63, 'raceEngineer': 'Ben Michell'},
        {'name': 'Williams', 'teamPrincipal': 'Jost Capito', 'nationality': 'British', 'yearsActive': 44,
         'raceEngineer': 'Paul Williams'},
        {'name': 'Haas', 'teamPrincipal': 'Guenther Steiner', 'nationality': 'American', 'yearsActive': 8,
         'raceEngineer': 'Ayao Komatsu'},
        {'name': 'Alfa Romeo', 'teamPrincipal': 'Frédéric Vasseur', 'nationality': 'Italian',
         'yearsActive': 72, 'raceEngineer': 'Ruth Buscombe'}]

    car_list = [
        {'model': 'Mercedes-AMG W13 E Performance', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,658lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Mercedes'},
        {'model': 'Red Bull Racing RB18', 'horsepower': '740bhp', 'engine': 'HRC 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Red Bull'},
        {'model': 'McLaren MCL36 Mercedes', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'McLaren'},
        {'model': 'Ferrari SF-75', 'horsepower': '740bhp', 'engine': 'Tipo 066/7 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Ferrari'},
        {'model': 'Alpine A522 Renault', 'horsepower': '740bhp', 'engine': 'Renault E22 90º V6',
         'weight': '1,753lbs', 'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Alpine'},
        {'model': 'AlphaTauri AT03', 'horsepower': '740bhp', 'engine': 'HRC 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'AlphaTauri'},
        {'model': 'Aston Martin AMR22 Mercedes', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Aston Martin'},
        {'model': 'Williams FW44 Mercedes', 'horsepower': '740bhp',
         'engine': 'Mercedes-AMG F1 M13 E Performance 90º V6', 'weight': '1,753lbs',
         'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Williams'},
        {'model': 'Haas VF-22 Ferrari', 'horsepower': '740bhp', 'engine': 'Ferrari Tipo 066/7 90º V6',
         'weight': '1,753lbs', 'gearbox': 'Paddle Operated 8 speed Automatic', 'constructor': 'Haas'},
        {'model': 'Alfa Romeo Racing C42 Ferrari', 'horsepower': '740bhp',
         'engine': 'Ferrari Tipo 066/7 90º V6', 'weight': '1,753lbs', 'gearbox': 'Paddle Operated 8 speed Automatic',
         'constructor': 'Alfa Romeo'}]

    race_list = [
        {'location': 'Bahrain - Sakhir', 'trackLength': '5.412km', 'date': '18/03-20/03', 'laps': 57,
         'time': '15:00-17:00'},
        {'location': 'Saudi Arabia - Jeddah', 'trackLength': '6.174km', 'date': '25/03-27/03', 'laps': 50,
         'time': '18:00-20:00'},
        {'location': 'Australia - Melbourne', 'trackLength': '5.303km', 'date': '08/04-10/04', 'laps': 58,
         'time': '06:00-08:00'},
        {'location': 'Italy - Imola', 'trackLength': '5.793km', 'date': '22/04-24/04', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'United States - Miami', 'trackLength': '5.410km', 'date': '06/05-/08/05', 'laps': 57,
         'time': '08:30-22:30'},
        {'location': 'Spain - Catalunya', 'trackLength': '4.655km', 'date': '20/05-22/05', 'laps': 66,
         'time': '14:00-16:00'},
        {'location': 'Monaco - Monaco', 'trackLength': '3.337km', 'date': '27/05-29/05', 'laps': 78,
         'time': '14:00-16:00'},
        {'location': 'Azerbaijan - Baku', 'trackLength': '6.003km', 'date': '10/06/-12/06', 'laps': 51,
         'time': '12:00-14:00'},
        {'location': 'Canada - Montreal', 'trackLength': '4.361km', 'date': '17/06-19/06', 'laps': 70,
         'time': '19:00-21:00'},
        {'location': 'Great Britain - Baku', 'trackLength': '6.003km', 'date': '10/06-12/06', 'laps': 51,
         'time': '12:00-14:00'},
        {'location': 'Great Britain - Silverstone', 'trackLength': '5.891km', 'date': '01/07-03/07',
         'laps': 52, 'time': '15:00-17:00'},
        {'location': 'Austria - Spielberg', 'trackLength': '	4.318km', 'date': '10/07-tbc/07', 'laps': 71,
         'time': '14:00-16:00'},
        {'location': 'France - Le Castellet', 'trackLength': '5.842km', 'date': '22/07-24/07', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'Hungary - Mogyoród', 'trackLength': '4.381km', 'date': '29/07-31/07', 'laps': 70,
         'time': '14:00-16:00'},
        {'location': 'Belgium - Spa', 'trackLength': '7.004km', 'date': '26/08-28/08', 'laps': 44,
         'time': '14:00-16:00'},
        {'location': 'Netherlands - Zandvoort', 'trackLength': '4.259km', 'date': '02/09-04/09', 'laps': 72,
         'time': '14:00-16:00'},
        {'location': 'Italy - Monza', 'trackLength': '5.793km', 'date': '09/09-11/09', 'laps': 53,
         'time': '14:00-16:00'},
        {'location': 'Singapore - Marina Bay', 'trackLength': '5.063km', 'date': '30/09-02/10',
         'laps': 61, 'time': '13:00-15:00'},
        {'location': 'Japan - Suzuka', 'trackLength': '5.807km', 'date': '07/10-09/10', 'laps': 53,
         'time': '06:00-08:00'},
        {'location': 'United States - Austin', 'trackLength': '5.513km', 'date': '21/10-23/10', 'laps': 56,
         'time': '20:00-22:00'},
        {'location': 'Mexico - Mexico City', 'trackLength': '4.304km', 'date': '28/10-30/10', 'laps': 71,
         'time': '20:00-22:00'},
        {'location': 'Brazi - São Paulo', 'trackLength': '4.309km', 'date': '11/11-13/11', 'laps': 71,
         'time': '20:00-22:00'},
        {'location': 'Abu Dhabi - United Arab Emirates', 'trackLength': '5.554km', 'date': '18/11-20/11', 'laps': 55,
         'time': '13:00-15:00'}]

    for i in driver_list:
        add_driver(i['name'], i['DOB'], i['height'], i['weight'], i['nationality'], i['driverNumber'],
                   i['seasonsWon'], i['podiumsWon'])

    for i in constructor_list:
        add_constructor(i['name'], i['teamPrincipal'], i['nationality'], i['yearsActive'], i['raceEngineer'])

    for i in car_list:
        add_car(i['model'], i['horsepower'], i['engine'], i['weight'], i['gearbox'], i['constructor'])

    for i in race_list:
        add_race(i['location'], i['trackLength'], i['date'], i['laps'], i['time'])


def add_driver(name, DOB, height, weight, nationality, driverNum, seasonsWon, podiumsWon):
    record = Driver.objects.get_or_create(name=name, DOB=DOB, height=height, weight=weight,
                                          nationality=nationality, driverNumber=driverNum, seasonsWon=seasonsWon,
                                          podiumsWon=podiumsWon)[0]
    record.save()
    print("Driver record \"" + name + "\" added.")
    return record


def add_constructor(name, teamPrincipal, nationality, yearsActive, raceEngineer):
    record = Constructor.objects.get_or_create(name=name, teamPrincipal=teamPrincipal, nationality=nationality,
                                               yearsActive=yearsActive, raceEngineer=raceEngineer)[0]
    record.save()
    print("Constructor record \"" + name + "\" added.")
    return record


def add_car(model, horsepower, engine, weight, gearbox, constructor):
    record = Car.objects.get_or_create(model=model, horsepower=horsepower, enginge=engine,
                                       weight=weight, gearbox=gearbox, constructor=constructor)[0]
    record.save()
    print("Car record \"" + model + "\" added.")
    return record


def add_race(location, trackLength, date, laps, time,overallRating):
    record = Race.objects.get_or_create(location=location, trackLength=trackLength, date=date, laps=laps, time=time)[0]
    record.save()
    print("Race record \"" + location + "\" added.")
    return record

def add_driverRating(driverID,userID,overallRating,personality,aggressiveness,awareness,experience,starts,pace,racecraft):
    record = DriverRating.objects.get_or_create(driverID=driverID, userID=userID)[0]
    record.personality=personality
    record.aggressiveness=aggressiveness
    record.awareness=awareness
    record.experience=experience
    record.starts=starts
    record.pace=pace
    record.racecraft=racecraft
    record.overallRating=overallRating
    record.save()
    print("Driver rating record for \"" + userID + "\" added.")
    return record
    
def add_carRating(carID,userID,overallRating,speed,aerodynamics,aesthetics,braking,engine):
    record = CarRating.objects.get_or_create(carID=carID, userID=userID)[0]
    record.overallRating=overallRating
    record.speed=spped
    record.aerodynamics=aerodynamics
    record.aesthetics=aesthetics
    record.braking=braking
    record.engine=record.engine
    record.save()
    print("Car rating record for \"" + userID + "\" added.")
    return record

def add_constructorRating(constructorID,userID,overallRating,teamPrincipal,raceStrategy,pitStop):
    record = ConstructorRating.objects.get_or_create(constructorID=constructorID, userID=userID)[0]
    record.overallRating=overallRating
    record.teamPrincipal=teamPrincipal
    record.raceStrategy=raceStrategy
    record.pitStop=pitStop
    record.save()
    print("Constructor rating record for \"" + userID + "\" added.")
    return record

#all seperate changes for about me, 3 favourites, password update, picture update
def add_user(username,password):
    record = User.objects.get_or_create(username=username,password=password)[0]
    record.save()
    print("User record \"" + username + "\" added.")
    return record


def update_picture(username, picture):
    pass


def update_about_me(username, aboutMe):
    record = User.objects.filter(username=username).update(aboutMe=aboutMe)


def update_favorites(username, favCar, favTeam, favDriver):
    record = User.objects.filter(username=username).update(favCar=favCar, favTeam=favTeam, favDriver=favDriver)


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    news_api.get_news()  # ensures database is populated before running timed calls
    print("Database Populated! This script will continue to run fetching updated news every hour.")
    news_api.run()
