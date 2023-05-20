from django.db import models


class Measurement(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    age = models.FloatField()
    waist = models.FloatField()
    
