from django.db import models
from subject.models import *


class Teacher(models.Model):
    tchName = models.CharField(max_length=255)
    tchSubject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tchDescription = models.TextField()
    tchWorks = models.BooleanField(default=False)