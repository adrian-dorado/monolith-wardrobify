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


# class Accessorie(models.Model):
#     HEADWEAR = "HEAD"
#     WATCHES = "WTCH"
#     BRACELET = "BRCLT"
#     NECKWEAR = "NECK"
#     GLOVES = "GLVE"
#     SCARF = "SCRF"
#     BELT = "BELT"
#     ACCESSORY_CHOICES = [
#         (HEADWEAR, "Headwear"),
#         (WATCHES, "Watches"),
#         (BRACELET, "Bracelets"),
#         (SCARF, "Scarves"),
#         (NECKWEAR, "Neckwear"),
#         (GLOVES, "Gloves"),
#         (BELT, "Belts"),
#     ]
#     name = models.CharField(max_length=32)
#     brand = models.CharField(max_length=32)
#     accessory_type = models.CharField(
#         max_length=12, choices=ACCESSORY_CHOICES, default=HEADWEAR
#     )


# class Bottom(models.Model):
#     PANTS = "PNTS"
#     SHORTS = "SHRT"
#     SKIRTS = "SKRT"
#     CAPRIS = "CRPI"
#     JOGGERS = "JOG"
#     BIKE_SHORTS = "BIKE"
#     SKORTS = "SKORT"
#     LEGGINGS = "LEGG"
#     BOTTOM_CHOICES = [
#         (PANTS, "Pants"),
#         (SHORTS, "Shorts"),
#         (SKIRTS, "Skirts"),
#         (CAPRIS, "Capris"),
#         (JOGGERS, "Joggers"),
#         (BIKE_SHORTS, "Bike Shorts"),
#         (SKORTS, "Skorts"),
#         (LEGGINGS, "Leggings"),
#     ]
#     name = models.CharField(max_length=32)
#     brand = models.CharField(max_length=32)
#     top_type = models.CharField(
#         max_length=12, choices=BOTTOM_CHOICES, default=PANTS
#     )


# class Footwear(models.Model):
#     SHOES = "SHOE"
#     HEELS = "HEEL"
#     SANDALS = "SAND"
#     SLIDES = "SLDE"
#     SOCKS = "SOCK"
#     BOOTS = "BOOT"
#     FOOTWEAR_CHOICES = [
#         (SHOES, "Shoes"),
#         (HEELS, "Heels"),
#         (SANDALS, "Sandals"),
#         (SLIDES, "Slides"),
#         (SOCKS, "Socks"),
#         (BOOTS, "Boots"),
#     ]
#     name = models.CharField(max_length=32)
#     brand = models.CharField(max_length=32)
#     top_type = models.CharField(
#         max_length=12, choices=FOOTWEAR_CHOICES, default=SHOES
#     )




# class Top(models.Model):
#     TSHIRT = "TEE"
#     JACKET = "JCKT"
#     SWEATER = "SWTR"
#     CARDIGAN = "CARD"
#     HOODIE = "HOOD"
#     VEST = "VST"
#     DRESS = "DRES"
#     COVERALLS = "CVRA"
#     TOP_CHOICES = [
#         (TSHIRT, "T-Shirts"),
#         (JACKET, "Jackets"),
#         (SWEATER, "Sweaters"),
#         (CARDIGAN, "Cardigans"),
#         (HOODIE, "Hoodies"),
#         (VEST, "Vests"),
#         (DRESS, "Dresses"),
#         (COVERALLS, "Coveralls"),
#     ]
#     name = models.CharField(max_length=32)
#     brand = models.CharField(max_length=32)
#     top_type = models.CharField(
#         max_length=12, choices=TOP_CHOICES, default=TSHIRT
#     )


# class Undergarment(models.Model):
#     UNDERSHIRTS = "UNSHRT"
#     BRAS = "BRA"
#     BIKINI_TOP = "BKNIT"
#     BIKINI_BOTTOM = "BKNIB"
#     UNDERWEAR = "UNWR"
#     SPORT_BRA = "SPTBR"
#     LINGERIE = "LNGR"
#     UNDERGARMENT_CHOICES = [
#         (UNDERSHIRTS, "Undershirts"),
#         (BRAS, "Bras"),
#         (BIKINI_TOP, "Bikini Top"),
#         (BIKINI_BOTTOM, "Bikini Bottom"),
#         (UNDERWEAR, "Underwear"),
#         (SPORT_BRA, "Sports Bra"),
#         (LINGERIE, "Lingerie"),
#     ]
#     name = models.CharField(max_length=32)
#     brand = models.CharField(max_length=32)
#     top_type = models.CharField(
#         max_length=15, choices=UNDERGARMENT_CHOICES, default=UNDERSHIRTS
#     )

