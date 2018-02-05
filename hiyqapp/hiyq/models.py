from django.db import models

class User(models.Model):
    userID=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    imageReference1=models.CharField(max_length=1000)
    imageReference2=models.CharField(max_length=1000)
    imageReference3=models.CharField(max_length=1000)
    gender=models.CharField(max_length=100)
    about=models.CharField(max_length=250)
    sexualPreference=models.CharField(max_length=250)
    premium=models.CharField(max_length=5)

class Event(models.Model):
    eventID=models.CharField(max_length=100)
    eventName=models.CharField(max_length=50)
    date_time=models.CharField(max_length=50)
    durarion=models.CharField(max_length=20)
    venue=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    imageReference1=models.CharField(max_length=1000)
    imageReference2=models.CharField(max_length=1000)
    imageReference3=models.CharField(max_length=1000)

class Match(models.Model):
    user1= models.ForeignKey(User, related_name= 'U1', on_delete=models.CASCADE)
    user2= models.ForeignKey(User, related_name='U2', on_delete=models.CASCADE)
    event= models.ForeignKey(Event, on_delete=models.CASCADE)
