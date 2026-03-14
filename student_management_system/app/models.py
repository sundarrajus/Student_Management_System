from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('admin','Admin'),
        ('staff','Staff')
    ])


class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    place = models.CharField(max_length=100)

    gender = models.CharField(max_length=10)

    state = models.CharField(max_length=50)

    skillset = models.CharField(max_length=200)

    added_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name