from django.contrib import admin
from .models import (
    Top,
    Accessorie,
    Bottom,
    Footwear,
    Undergarment,
)
# Register your models here.

admin.site.register(Top)
admin.site.register(Accessorie)
admin.site.register(Bottom)
admin.site.register(Footwear)
admin.site.register(Undergarment)