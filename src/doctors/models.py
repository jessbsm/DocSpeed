from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
#MVC Model View Controller



class Doctor(models.Model):
	name = models.CharField(max_length=120)
	speciality = models.TextField(default='médecine générale')
	num_street = models.IntegerField(default=0)
	type_street = models.TextField(default='rue')
	name_street = models.TextField(default='Ampère')
	city = models.TextField(default='Champs-sur-Marne')
	address = models.TextField(default='77420 Champs-sur-Marne')
	phone = models.CharField(max_length=14)
	schedule = models.TextField(default='Du lundi au vendredi de 9h à 17h')
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	nb_person = models.IntegerField(default=0)
	waiting_room = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_doctor_url(self):
		return reverse("doctor:detail",kwargs={"id": self.id})



class Patient(models.Model):
	name = models.CharField(max_length=120)
	num_street = models.IntegerField()
	type_street = models.TextField()
	name_street = models.TextField()
	city = models.TextField(default='Champs-sur-Marne')
	country = models.TextField(default='France')
	doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, default=1)	

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_patient_url(self):
		return reverse("patient:detail",kwargs={"id": self.id})



import json
import urllib.request


class adress:
    def __init__(self, n, road, name, city):
        self.number = n
        self.road_type = road
        self.road_name = name
        self.city = city
        
    def get_url_adress(self):
        ''' rend l'url de l'api google map, pour traduire les adresses en coordonnées'''
        
        part_fix = "http://maps.googleapis.com/maps/api/geocode/json?"
        street_number = "address=" + self.number
        roads =  self.road_type + "+" + self.road_name
        city = self.city
        
        part_fix2 = "&sensor=false"
               
        url = part_fix + street_number + "+" + roads + "," + city + part_fix2
        #print(url)
        return(url)
   
    def get_lat_lng(self):
        '''permet d'obtenir les coordonnees latitude et longitude de l'adresse'''
        url = self.get_url_adress()        
        
        response = urllib.request.urlopen(url).read()
        doc = json.loads(response.decode('utf-8'))
        lat = doc['results'][0]['geometry']['location']['lat']
        long = doc['results'][0]['geometry']['location']['lng']
        return [lat,long]
    
#************TEST********************
    
#url_adresse = get_url_adresse("6", "rue", "sartoris", "La Garenne Colombes")
#GPS = get_lat_lng(url_adresse)


'''Calcul du temps de trajet'''
def get_url_journey(depart, arrival, mode = "driving"):
    ''' rend l'url de l'api google map, les différents modes sont:
    driving(par défaut), walking, bicycling, transit '''
    
    depart_str = str(depart[0]) + "," + str(depart[1])
    arrival_str = str(arrival[0]) + "," + str(arrival[1])
    
    part_fix = "http://maps.googleapis.com/maps/api/distancematrix/json?"
    departure = "origins=" + depart_str
    arrivals = "&destinations=" + arrival_str
    part_fix2 = "&sensor=false"
           
    url_duration = part_fix + departure + arrivals + part_fix2
    
    if mode != "driving":
        option_walk = "&mode=" + mode
        url_duration = url_duration + option_walk
 
    return(url_duration)

def get_duration(url_duration):
    
    response = urllib.request.urlopen(url_duration).read()
    doc = json.loads(response.decode('utf-8'))
    duree = doc['rows'][0]['elements'][0]['duration']['text']
    duree1 = duree.split
    duree_real = int(duree1[0])
    return(duree_real)
    
    
'''Calcul du temps d'attente entre un medecin et l'utilisateur'''
def waiting_time(waiting_room, adress_user, adress_medecin):
    Gps_user = adress_user.get_lat_lng()
    Gps_medecin = adress_medecin.get_lat_lng()
    
    url_journey = get_url_journey(Gps_user, Gps_medecin)
    print(url_journey)
    duration_journey = get_duration(url_journey)
    print(duration_journey)
    time = waiting_room*15 + duration_journey
    
    return time




