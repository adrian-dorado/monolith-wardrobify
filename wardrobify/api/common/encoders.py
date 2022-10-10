from common.json import ModelEncoder
from .models import (
    Top,
    Accessorie,
    Bottom,
    Footwear,
    Undergarment,
)


class TopEncoder(ModelEncoder):
    model = Top
    properties = ["id", "name", "brand", "top_type"]


class BottomEncoder(ModelEncoder):
    model = Bottom
    properties = ["id", "name", "brand", "bottom_type"]


class UndergarmentEncoder(ModelEncoder):
    model = Undergarment
    properties = ["id", "name", "brand", "undergarment_type"]


class AccessoriesEncoder(ModelEncoder):
    model = Accessorie
    properties = ["id", "name", "brand", "accessory_type"]


class FootwearEncoder(ModelEncoder):
    model = Footwear
    properties = ["id", "name", "brand", "footwear_type"]


