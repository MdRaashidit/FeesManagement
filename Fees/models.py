from django.db import models



class Student(models.Model):

    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    phone = models.IntegerField()
    roll = models.CharField(max_length=20, unique=True)
