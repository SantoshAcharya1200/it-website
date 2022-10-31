from django.db import models

# Create your models here.

class Destination(models.Model):

    img = models.ImageField(upload_to="pics")
    des = models.CharField(max_length=400)
    title=  models.CharField(max_length=100)
