from django.db import models

# Create your models here.
class Subject(models.Model):
    sbjName = models.CharField(max_length=255)
    sbjDescription = models.TextField()
    sbjAgreed = models.BooleanField(default=False)

