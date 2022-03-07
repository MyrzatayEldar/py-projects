from django.db import models


class ProfileInfo(models.Model):
    first_name = models.CharField(max_length=255)  # имя
    last_name = models.CharField(max_length=255)  # отчество
    surname = models.CharField(max_length=255)  # фамилия
    birthday = models.DateField()  # день рождения
    email = models.EmailField(max_length=255)  # емайл

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ProfileLoginAndPassword(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.login


class JaiModel(models.Model):
    name = models.CharField(max_length=100)
    how_many = models.IntegerField()


