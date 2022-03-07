from django.db import models

# Create your models here.
class Student(models.Model):
    stdFirstName = models.CharField(max_length=255)
    stdSurname = models.CharField(max_length=255)
    stdDayOfBirth = models.DateField()
    stdIIN = models.CharField(max_length=12)
    stdPrSubject1 = models.CharField(max_length=255)
    stdPrSubject2 = models.CharField(max_length=255)