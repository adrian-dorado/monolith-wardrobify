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

    def __str__(self):
        return f"{self.name}"


class Outfit(models.Model):
    outfit_name = models.CharField(max_length=120)
    closet = models.ForeignKey(Closet, related_name="outfit", on_delete=models.CASCADE)
    accessories = models.ManyToManyField(Accessorie, blank=True)
    top = models.ManyToManyField(Top, blank=True)
    undergarment = models.ManyToManyField(Undergarment, blank=True)
    bottom = models.ManyToManyField(Bottom, blank=True)
    footwear = models.ManyToManyField(Footwear, blank=True)

    def __str__(self):
        return f"{self.outfit_name}"