from django.db import models

# Create your models here.

class Worldle(models.Model):

    img = models.ImageField(upload_to="pics")
    title=  models.CharField(max_length=100)
