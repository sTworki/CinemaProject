from django.db import models


# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=50)
