from django.db import models

# Create your models here.


class Stat(models.Model):
    name = models.CharField(max_length=50)
    att = models.IntegerField()
    yds = models.IntegerField()
    avg = models.FloatField()
    long = models.IntegerField()
    td = models.IntegerField()
