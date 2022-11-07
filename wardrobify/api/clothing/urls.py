from django.urls import path

from .views import list_categories, category_details, list_clothing_items, clothing_item_details, list_outfits

urlpatterns = [
    path("categories/", list_categories, name="categories_list"),
    path("categories/<int:pk>/", category_details, name="category_details"),
    path("", list_clothing_items, name="clothing_items_list"),
    path("<int:pk>/", clothing_item_details, name="clothing_details"),
    path("outfits/", list_outfits, name="outfits_list"),
    # path("<int:pk>/", clothing_item_details, name="clothing_details"),
]
