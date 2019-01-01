# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Words(models.Model):
    name = models.CharField(max_length=75)
    repeatedValue = models.IntegerField(default=0)
