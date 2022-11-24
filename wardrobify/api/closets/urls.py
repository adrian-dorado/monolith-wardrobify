from django.urls import path
from .views import closet_list, closet_details

urlpatterns = [
    path("", closet_list, name="closets_list"),
    path("<int:pk>/", closet_details, name="closet_detail")
]