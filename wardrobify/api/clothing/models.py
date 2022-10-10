from django.db import models

# Create your models here.


class Accessorie(models.Model):
    HEADWEAR = "HEAD"
    WATCHES = "WTCH"
    BRACELET = "BRCLT"
    NECKWEAR = "NECK"
    GLOVES = "GLVE"
    SCARF = "SCRF"
    BELT = "BELT"
    ACCESSORY_CHOICES = [
        (HEADWEAR, "Headwear"),
        (WATCHES, "Watches"),
        (BRACELET, "Bracelets"),
        (SCARF, "Scarves"),
        (NECKWEAR, "Neckwear"),
        (GLOVES, "Gloves"),
        (BELT, "Belts"),
    ]
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    accessory_type = models.CharField(
        max_length=12, choices=ACCESSORY_CHOICES, default=HEADWEAR
    )


class Top(models.Model):
    TSHIRT = "TEE"
    JACKET = "JCKT"
    SWEATER = "SWTR"
    CARDIGAN = "CARD"
    HOODIE = "HOOD"
    VEST = "VST"
    DRESS = "DRES"
    COVERALLS = "CVRA"
    TOP_CHOICES = [
        (TSHIRT, "T-Shirts"),
        (JACKET, "Jackets"),
        (SWEATER, "Sweaters"),
        (CARDIGAN, "Cardigans"),
        (HOODIE, "Hoodies"),
        (VEST, "Vests"),
        (DRESS, "Dresses"),
        (COVERALLS, "Coveralls"),
    ]
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    top_type = models.CharField(
        max_length=12, choices=TOP_CHOICES, default=TSHIRT
    )


class Bottom(models.Model):
    PANTS = "PNTS"
    SHORTS = "SHRT"
    SKIRTS = "SKRT"
    CAPRIS = "CRPI"
    JOGGERS = "JOG"
    BIKE_SHORTS = "BIKE"
    SKORTS = "SKORT"
    LEGGINGS = "LEGG"
    BOTTOM_CHOICES = [
        (PANTS, "Pants"),
        (SHORTS, "Shorts"),
        (SKIRTS, "Skirts"),
        (CAPRIS, "Capris"),
        (JOGGERS, "Joggers"),
        (BIKE_SHORTS, "Bike Shorts"),
        (SKORTS, "Skorts"),
        (LEGGINGS, "Leggings"),
    ]
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    top_type = models.CharField(
        max_length=12, choices=BOTTOM_CHOICES, default=PANTS
    )


class Undergarment(models.Model):
    UNDERSHIRTS = "UNSHRT"
    BRAS = "BRA"
    BIKINI_TOP = "BKNIT"
    BIKINI_BOTTOM = "BKNIB"
    UNDERWEAR = "UNWR"
    SPORT_BRA = "SPTBR"
    LINGERIE = "LNGR"
    UNDERGARMENT_CHOICES = [
        (UNDERSHIRTS, "Undershirts"),
        (BRAS, "Bras"),
        (BIKINI_TOP, "Bikini Top"),
        (BIKINI_BOTTOM, "Bikini Bottom"),
        (UNDERWEAR, "Underwear"),
        (SPORT_BRA, "Sports Bra"),
        (LINGERIE, "Lingerie"),
    ]
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    top_type = models.CharField(
        max_length=15, choices=UNDERGARMENT_CHOICES, default=UNDERSHIRTS
    )

class Footwear(models.Model):
    SHOES = "SHOE"
    SANDALS = "SAND"
    SLIDES = "SLDE"
    SOCKS = "SOCK"
    BOOTS = "BOOT"
    FOOTWEAR_CHOICES = [
        (SHOES, "Shoes"),
        (SANDALS, "Sandals"),
        (SLIDES, "Slides"),
        (SOCKS, "Socks"),
        (BOOTS, "Boots"),
    ]
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    top_type = models.CharField(
        max_length=12, choices=FOOTWEAR_CHOICES, default=SHOES
    )

