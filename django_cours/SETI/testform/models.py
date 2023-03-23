from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50, null = True)
    last_name = models.CharField(max_length=50, null = True)
    contact = models.IntegerField(null = True)
    email = models.EmailField(max_length=254, null = True)
    age = models.IntegerField(null = True)

    class Meta:
        db_table = "student"

class Employee(models.Model):
    eid = models.CharField(max_length = 10)
    ename = models.CharField(max_length = 150)
    econtact = models.CharField(max_length = 150)

    class Meta:
        db_table = "employee"
