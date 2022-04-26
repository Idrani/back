from django.db import models
from django.db.models import Model
# Create your models here.
class VAL(models.Model):
    NumOF = models.IntegerField(primary_key=True)
    NumV = models.IntegerField()
    valide = models.IntegerField()
    date1 = models.CharField(default='', max_length=100)
    date2 = models.CharField(default='', max_length=100)
    date3 = models.CharField(default='', max_length=100)
    date4 = models.CharField(default='', max_length=100)
    date5 = models.CharField(default='', max_length=100)