import os
import news_api
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')

import django
django.setup()
from rango.models import Driver,Constructor,Car,Race

news_api.get_news()  # ensures database is populated before running timed calls
news_api.run()

def populate():
    
    # 1.0 pictures???
    # 2.0 updating foreign keys with drivers, cars, constructors in models.py and then dictionaries.
    # 3.0 adding_cars, etc functions.
    # 4.0 car categories hard to find.
    # i still need to add 16 races - libby
    
    driver_list = [{'name':'Lewis Hamilton','DOB':'07/01/1985','picture':,'height':'1.74m','weight':'73kg','nationality':'British','driverNumber':44,'seasonsWon':7,'podiumsWon':182},{'name':'George Russell','DOB':'15/02/1998','picture':,'height':'1.85m','weight':'70kg','nationality':'British','driverNumber':63,'seasonsWon':0,'podiumsWon':1},{'name':'Max Verstappen','DOB':'30/09/1997','picture':,'height':'1.81m','weight':'72kg','nationality':'Belgian-Dutch','driverNumber':'1','seasonsWon':1,'podiumsWon':60},{'name':'Sergio Perez','DOB':'26/01/1990','picture':,'height':'1.73m','weight':'63kg','nationality':'Mexican','driverNumber':11,'seasonsWon':0,'podiumsWon':15},{'name':'Lando Norris','DOB':'13/11/1999','picture':,'height':'1.7m','weight':'66kg','nationality':'British','driverNumber':4,'seasonsWon':0,'podiumsWon':5},{'name':'Daniel Ricciardo','DOB':'01/07/1989','picture':,'height':'1.8m','weight':'72kg','nationality':'Australian','driverNumber':3,'seasonsWon':0,'podiumsWon':32},{'name':'Carlos Sainz','DOB':'01/09/1994','picture':,'height':'1.78m','weight':'64kg','nationality':'Spanish','driverNumber':3,'seasonsWon':0,'podiumsWon':6},{'name':'Charles Leclerc','DOB':'16/10/1997','picture':,'height':'1.8m','weight':'69kg','nationality':'Monocan','driverNumber':16,'seasonsWon':0,'podiumsWon':13},{'name':'Fernando Alonso','DOB':'29/07/1981','picture':,'height':'1.71m','weight':'68kg','nationality':'Spanish','driverNumber':14,'seasonsWon':2,'podiumsWon':98},{'name':'Esteban Ocon','DOB':'17/09/1996','picture':,'height':'1.86m','weight':'66kg','nationality':'French','driverNumber':31,'seasonsWon':0,'podiumsWon':2},{'name':'Pierre Gasly','DOB':'07/02/1996','picture':,'height':'1.77m','weight':'70kg','nationality':'French','driverNumber':10,'seasonsWon':0,'podiumsWon':3},{'name':'Yuki Tsunoda','DOB':'11/05/2000','picture':,'height':'1.59m','weight':'54kg','nationality':'Japanese','driverNumber':22,'seasonsWon':0,'podiumsWon':0},{'name':'Sebastian Vettel','DOB':'3/07/1987','picture':,'height':'1.75m','weight':'62kg','nationality':'German','driverNumber':5,'seasonsWon':4,'podiumsWon':122},{'name':'Lance Stroll','DOB':'29/10/1998','picture':,'height':'1.82m','weight':'70kg','nationality':'Canadian','driverNumber':18,'seasonsWon':0,'podiumsWon':3,}{'name':'Alexander Albon','DOB':'23/03/1996','picture':,'height':'1.86m','weight':'73kg','nationality':'Thai','driverNumber':23,'seasonsWon':0,'podiumsWon':2},{'name':'Nicholas Latifi','DOB':'29/07/1995','picture':,'height':'1.85m','weight':'73kg','nationality':'Canadian','driverNumber':6,'seasonsWon':0,'podiumsWon':0},{'name':'Mick Schumacher','DOB':'22/03/1999','picture':,'height':'1.77m','weight':'67kg','nationality':'German','driverNumber':47,'seasonsWon':0,'podiumsWon':0},{'name':'Valtteri Bottas','DOB':'28/08/1989','picture':,'height':'1.73m','weight':'69kg','nationality':'Finnish','driverNumber':77,'seasonsWon':0,'podiumsWon':67},{'name':'Guanyu Zhou','DOB':'30/05/1999','picture':,'height':'1.75m','weight':'63kg','nationality':'Chinese','driverNumber':24,'seasonsWon':0,'podiumsWon':0}]
    
    constructor_list = [{'name':'Mercedes AMG Petronas F1 Team','teamPrincipal':'Totto Wolff','nationality':'German','yearsActive':68,'raceEngineer':'Peter Bonnington'},{'name':'Oracle Red Bull Racing','teamPrincipal':'Christian Horner','nationality':'Austrian','yearsActive':17,'raceEngineer':'Gianpiero Lambiase'},{'name':'McLaren F1 Team','teamPrincipal':'Zak Brown','nationality':'British','yearsActive':56,'raceEngineer':'William Joseph'},{'name':'Scuderia Ferrari','teamPrincipal':'Mattia Binotto','nationality':'Italian','yearsActive':72,'raceEngineer':'Riccardo Adami'},{'name':'Alpine F1 Team','teamPrincipal':'Otmar Szafnauer','nationality':'French','yearsActive':1,'raceEngineer':'Karel Loos'},{'name':'Scuderia AlphaTauri','teamPrincipal':'Franz Tost','nationality':'Italian','yearsActive':18,'raceEngineer':'Pierre Hamelin'},{'name':'Aston Martin Aramco Cognizant F1 Team','teamPrincipal':'Lawrence Stroll','nationality':'British','yearsActive':63,'raceEngineer':'Ben Michell'},{'name':'Williams Racing','teamPrincipal':'Jost Capito','nationality':'British','yearsActive':44,'raceEngineer':'Paul Williams'},{'name':'Haas F1 Team','teamPrincipal':'Guenther Steiner','nationality':'American','yearsActive':8,'raceEngineer':'Ayao Komatsu'},{'name':'Alfa Romeo F1 Team Orlen','teamPrincipal':'Frédéric Vasseur','nationality':'Italian','yearsActive':72,'raceEngineer':'Ruth Buscombe'}]
    
    car_list = [{'model':,'horsePower':,'engineSupplier':,'picture':,'gearbox':}]
    
    race_list = [{'location':'Bahrain - Sakhir','trackLength':'5.412km','date':'18-20/03/2022','laps':57,'time':'15:00-17:00'},{'location':'Saudi Arabia - Jeddah','trackLength':'6.174km','date':'25-27/03/2022','laps':50,'time':'18:00-20:00'},{'location':'Australia - Melbourne','trackLength':'5.303km','date':'08-10/04/2022','laps':58,'time':'06:00-08:00'},{'location':'Italy - Monza','trackLength':'5.793km','date':'22-24/04/2022','laps':53,'time':'14:00-16:00'},{'location':'United States - Miami','trackLength':'5.410km','date':'06-08/05/2022','laps':57,'time':'08:30-22:30'},{'location':'Spain - Catalunya','trackLength':'4.655km','date':'20-22/05/2022','laps':66,'time':'14:00-16:00'}]
    
    
    
    
    


