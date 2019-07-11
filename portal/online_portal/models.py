# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now_add=True,editable=False)

class account(TimeStampedModel):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    dob=models.DateTimeField()
    blood=models.CharField(max_length=20)
    password=models.CharField(max_length=20)



