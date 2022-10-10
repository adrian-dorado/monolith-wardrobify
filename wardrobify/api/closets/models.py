from django.db import models
from clothing.models import (
    Accessorie,
    Bottom,
    Footwear,
    Top,
    Undergarment,
)

# Create your models here.


class Closet(models.Model):
    name = models.CharField(max_length=120)
    closet_number = models.SmallIntegerField()
    closet_size = models.SmallIntegerField()


class Outfit(models.Model):
    outfit_name = models.CharField(max_length=120)
    accessories = models.ManyToManyField(Accessorie)
    bottom = models.ManyToManyField(Bottom)
    footwear = models.ManyToManyField(Footwear)
    top = models.ManyToManyField(Top)
    undergarment = models.ManyToManyField(Undergarment)
