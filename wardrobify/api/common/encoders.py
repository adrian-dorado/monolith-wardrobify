from common.json import ModelEncoder

from clothing.models import Outfit, Category, ClothingItem
from closets.models import Closet


class ClosetEncoder(ModelEncoder):
    model = Closet
    properties = ["id", "name", "closet_number", "closet_size"]


class CategoryEncoder(ModelEncoder):
    model = Category
    properties = ["id", "name"]



class OutfitEncoder(ModelEncoder):
    model = Outfit
    properties = ["id", "name", "desc", "date_created"]

    def get_extra_data(self, o):
        return {
            "closet": o.closet.name,
            "closet_number": o.closet.closet_number
        }

class ClothingItemEncoder(ModelEncoder):
    model = ClothingItem
    properties = ["id", "name", "category"]


    def get_extra_data(self, o):
        return {
            "outfit_name": o.outfit.name,
            "category": o.category.name,
        }

