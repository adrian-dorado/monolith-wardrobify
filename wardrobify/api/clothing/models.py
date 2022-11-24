from django.db import models
from closets.models import Closet

# Create your models here.


class Outfit(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    closet = models.ForeignKey(
        Closet,
        related_name="outfits",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class ClothingItem(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    category = models.ForeignKey(
        Category,
        related_name="item_categories",
        on_delete=models.CASCADE
    )
    outfit = models.ForeignKey(
        Outfit,
        related_name="outfit_items",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} - {self.outfit}"
