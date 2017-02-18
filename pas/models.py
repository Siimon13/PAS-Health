from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length = 200, null = False)
    last_name = models.CharField(max_length = 200, null = False)
    ethnicity = models.CharField(max_length = 200, null = False)
    gender = models.CharField(max_length = 200, null = False)
    current_weight = models.CharField(max_length = 200, null = False)
    goal_weight = models.CharField(max_length = 200, null = False)
