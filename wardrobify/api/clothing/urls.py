from django.urls import path

from .views import (
    list_accessories,
    list_bottoms,
    list_footwear,
    list_tops,
    list_undergarments,
    top_details,
    bottom_details,
    undergarment_details,
    footwear_details,
    accessory_details,
)

urlpatterns = [
    path("accessories/", list_accessories, name="accessories_list"),
    path("accessories/<int:pk>/", accessory_details, name="accessory_details"),
    path("bottoms/", list_bottoms, name="bottoms_list"),
    path("bottoms/<int:pk>/", bottom_details, name="bottom_details"),
    path("footwear/", list_footwear, name="footwear_list"),
    path("footwear/<int:pk>/", footwear_details, name="footwear_details"),
    path("tops/", list_tops, name="tops_list"),
    path("tops/<int:pk>/", top_details, name="top_details"),
    path("undergarments/", list_undergarments, name="undergarments_list"),
    path("undergarments/<int:pk>/", undergarment_details, name="undergarment_details"),
]
