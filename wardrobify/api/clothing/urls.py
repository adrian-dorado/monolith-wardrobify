from django.urls import path

from .views import list_categories, category_details

urlpatterns = [
    path("categories/", list_categories, name="categories_list"),
    path("categories/<int:pk>/", category_details, name="category_details"),
]
