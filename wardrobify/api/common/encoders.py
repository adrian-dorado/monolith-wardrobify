from common.json import ModelEncoder

from clothing.models import Outfit, Category, ItemCategory, OutfitItem
from closets.models import Closet


class ClosetEncoder(ModelEncoder):
    model = Closet
    properties = ["id", "name", "closet_number", "closet_size"]


class CategoryEncoder(ModelEncoder):
    model = Category
    properties = ["id", "name"]


class ItemCategoryEncoder(ModelEncoder):
    model = ItemCategory
    properties = ["id", "name", "category"]

    def get_extra_data(self, o):
        return {"category": o.category.name}

class OutfitEncoder(ModelEncoder):
    model = Outfit
    properties = ["id", "name", "desc", "date_created", "closet"]

    encoders = {"closet": ClosetEncoder()}



class OutfitItemEncoder(ModelEncoder):
    model = OutfitItem
    properties = ["id", "name", "outfit", "item_category"]

    encoders = {
        "outfit": OutfitEncoder(),
        "item_category": ItemCategoryEncoder()
    }


# class TopEncoder(ModelEncoder):
#     model = Top
#     properties = ["id", "name", "brand", "top_type"]


# class BottomEncoder(ModelEncoder):
#     model = Bottom
#     properties = ["id", "name", "brand", "bottom_type"]


# class UndergarmentEncoder(ModelEncoder):
#     model = Undergarment
#     properties = ["id", "name", "brand", "undergarment_type"]


# class AccessoriesEncoder(ModelEncoder):
#     model = Accessorie
#     properties = ["id", "name", "brand", "accessory_type"]


# class FootwearEncoder(ModelEncoder):
#     model = Footwear
#     properties = ["id", "name", "brand", "footwear_type"]


# class ClosetsEncoder(ModelEncoder):
#     model = Closet
#     properties = ["id", "name", "closet_number", "closet_size"]


# class OutfitsEncoder(ModelEncoder):
#     model = Outfit
#     properties = [
#         "id",
#         "outfit_name",
#         "accessories",
#         "bottom",
#         "footwear",
#         "top",
#         "undergarment"
#     ]

#     def get_extra_data(self, o):
#         return {
#             "accessories": o.accessories.name,

#         }

# encoders = {
#     "accessories": AccessoriesEncoder(),
#     "bottom": BottomEncoder(),
#     "footwear": FootwearEncoder(),
#     "top": TopEncoder(),
#     "undergarment": UndergarmentEncoder()
# }
