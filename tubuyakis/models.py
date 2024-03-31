from django.db import models

# Create your models here.


class Tweet(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    

