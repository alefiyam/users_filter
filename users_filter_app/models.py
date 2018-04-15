# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class User(models.Model):
    resume = models.BooleanField(default=False)
    name = models.CharField(max_length=500)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    work_exp = models.CharField(max_length=10)
    anaytics_in_exp = models.CharField(max_length=10)
    current_location = models.CharField(max_length=100)
    corrected_location = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    ctc = models.CharField(max_length=10,blank=True)
    current_employer = models.CharField(max_length=100,blank=True)
    current_designation = models.CharField(max_length=30,blank=True)
    skills = models.CharField(max_length=100,blank=True)
    UG_Course = models.CharField(max_length=100,blank=True)
    UG_Institute_Name = models.CharField(max_length=100,blank=True)
    trier_1 = models.CharField(max_length=10,blank=True)
    UG_Passing_Year = models.CharField(max_length=4,blank=True) 
    PG_Course = models.CharField(max_length=100,blank=True)
    Correct_PG_Course = models.CharField(max_length=100,blank=True)
    PG_Institute_Name = models.CharField(max_length=100,blank=True)
    trier_1 = models.CharField(max_length=10,blank=True)
    PG_Passing_Year = models.CharField(max_length=4,blank=True)
    Post_PG_Course = models.CharField(max_length=100,blank=True) 
    Correct_Post_PG = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']