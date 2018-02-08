# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=30, unique=True)
    logo = models.ImageField(upload_to = 'img')

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to = 'img')
    university = models.ForeignKey(University, related_name='faculty')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length= 250, unique=True)
    picture = models.ImageField(upload_to = 'img')
    faculty = models.ForeignKey(Faculty, related_name='doctor')
    university = models.ForeignKey(University ,related_name='doc')
    
    RATE_CHOICES = (
        ('1' , 'very weak'),
        ('2' , 'weak'),
        ('3', 'good'),
        ('4' , 'very good'),
        ('5', 'excellent'),
    )

    rate = models.CharField(
        max_length= 1,
        choices = RATE_CHOICES,
        default = '1'
    )

    def __str__(self):
        return self.name

 