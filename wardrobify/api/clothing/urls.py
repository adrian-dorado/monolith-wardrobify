from django.urls import path

from .views import list_categories, category_details, list_item_categories, item_category_details

urlpatterns = [
    path("categories/", list_categories, name="categories_list"),
    path("categories/<int:pk>/", category_details, name="category_details"),
    path("item_categories/", list_item_categories, name="item_categories_list"),
    path("item_categories/<int:pk>/", item_category_details, name="item_category_details"),
]
