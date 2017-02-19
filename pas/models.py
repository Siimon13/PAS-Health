from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 200, null = False)
    last_name = models.CharField(max_length = 200, null = False)
    ethnicity = models.CharField(max_length = 200, null = False)
    gender = models.CharField(max_length = 200, null = False)
    current_weight = models.FloatField(null = False)
    goal_weight = models.FloatField(null = False)
    age = models.FloatField(null = False)
    lifestyle = models.CharField(max_length = 200, null = False)
    current_height = models.FloatField(null = False)
    current_diet = models.CharField(max_length = 200, null = True)
    hashid = models.CharField(max_length = 50, null = False)
