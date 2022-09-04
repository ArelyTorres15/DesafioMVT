from django.db import models

# Create your models here.

class Madre(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    fecha_nac= models.DateField()

class Padre(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    fecha_nac= models.DateField()

class Hermano(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    fecha_nac= models.DateField()
