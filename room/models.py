from django.db import models

class Room(models.Model):
    # name field
    name = models.CharField(max_length=200)
    # slug field
    slug = models.SlugField(unique=True)