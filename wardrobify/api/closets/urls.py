from django.urls import path
from .views import closet_list, closet_details

urlpatterns = [
    path("all/", closet_list, name="closets_list")
]