from django.db import models

# Create your models here.


class Closet(models.Model):
    name = models.CharField(max_length=120)
    closet_number = models.SmallIntegerField(unique=True)
    closet_size = models.SmallIntegerField()

    def __str__(self):
        return self.name

