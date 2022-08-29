from django.db import models


class Familia(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    altura_m = models.IntegerField()
    sexo_F_M = models.CharField(max_length=3)


    