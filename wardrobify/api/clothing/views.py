from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.encoders import CategoryEncoder, ClothingItemEncoder, OutfitEncoder
from .models import Category, ClothingItem, Outfit, Closet

# # ------------------- Category VIEWS --------------------


@require_http_methods(["GET", "POST"])
def list_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return JsonResponse({"Categories": categories}, encoder=CategoryEncoder)
    else:
        content = json.loads(request.body)
        category = Category.objects.create(**content)
        return JsonResponse({"Category Created": category}, encoder=CategoryEncoder)


@require_http_methods(["GET", "PUT", "DELETE"])
def category_details(request, pk):
    if request.method == "GET":
        try:
            category = Category.objects.get(id=pk)
            return JsonResponse({"Category Details": category}, encoder=CategoryEncoder, safe=False)
        except Category.DoesNotExist:
            response = JsonResponse({"Message": "Category does not exist"})
            response.status_code = 404
            return response
    elif request.method == "PUT":
        content = json.loads(request.body)
        try:
            category = Category.objects.filter(id=pk).update(**content)
            return JsonResponse({"Category Updated": category}, encoder=CategoryEncoder, safe=False)
        except Category.DoesNotExist:
            response = JsonResponse({"Message": "Category does not exist"})
            response.status_code = 404
            return response
    else:
        try:
            category = Category.objects.get(id=pk)
            category.delete()
            return JsonResponse({"Category Deleted": category}, encoder=CategoryEncoder, safe=False)
        except Category.DoesNotExist:
            response = JsonResponse({"Message": "Category does not exist"})
            response.status_code = 404
            return response


# ------------------- Clothing Item VIEWS --------------------


@require_http_methods(["GET", "POST"])
def list_clothing_items(request):
    if request.method == "GET":
        clothing_items = ClothingItem.objects.all()
        return JsonResponse({"Clothing Items": clothing_items}, encoder=ClothingItemEncoder)
    else:
        content = json.loads(request.body)
        try:
            category = Category.objects.get(name=content["category"])
            content["category"] = category
        except Category.DoesNotExist:
            return JsonResponse(
                {"Message": "Category does not exist"},
                status=400
            )
        try:
            outfit = Outfit.objects.get(id=content["outfit"])
            content["outfit"] = outfit
        except Outfit.DoesNotExist:
            return JsonResponse(
                {"Message": "Outfit does not exist"},
                status=400
            )
        clothing_item = ClothingItem.objects.create(**content)
        return JsonResponse({"Clothing Item Created": clothing_item}, encoder=ClothingItemEncoder, safe=False)


@require_http_methods(["GET", "PUT", "DELETE"])
def clothing_item_details(request, pk):
    if request.method == "GET":
        try:
            clothing_item = ClothingItem.objects.get(id=pk)
            return JsonResponse({"Item Category": clothing_item}, encoder=ClothingItemEncoder, safe=False)
        except ClothingItem.DoesNotExist:
            response = JsonResponse({"Message": "Clothing Item Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "PUT":
        content = json.loads(request.body)
        try:
            category = Category.objects.get(name=content["category"])
            content["category"] = category
        except Category.DoesNotExist:
            return JsonResponse(
                {"Message": "Category Does Not Exist"},
                status=400,
            )
        try:
            outfit = Outfit.objects.get(id=content["outfit"])
            content["outfit"] = outfit
        except Outfit.DoesNotExist:
            return JsonResponse(
                {"Message": "Outfit does not exist"},
                status=400
            )
        try:
            clothing_item = ClothingItem.objects.filter(id=pk).update(**content)
            return JsonResponse({"Clothing Item Updated": clothing_item}, encoder=ClothingItemEncoder, safe=False)
        except ClothingItem.DoesNotExist:
            response = JsonResponse({"Message": "Item Category Does Not Exist"})
            response.status_code = 404
            return response
    else:
        try:
            clothing_item = ClothingItem.objects.get(id=pk)
            clothing_item.delete()
            return JsonResponse({"Category Deleted": clothing_item}, encoder=ClothingItemEncoder, safe=False)
        except ClothingItem.DoesNotExist:
            response = JsonResponse({"Message": "Category does not exist"})
            response.status_code = 404
            return response
    

# ------------------- Outfit VIEWS --------------------


@require_http_methods(["GET", "POST"])
def list_outfits(request):
    if request.method == "GET":
        outfits = Outfit.objects.all()
        return JsonResponse({"Outfits": outfits}, encoder=OutfitEncoder)
    else:
        content = json.loads(request.body)
        try:
            closet = Closet.objects.get(id=content["closet"])
            content["closet"] = closet
        except Closet.DoesNotExist:
            return JsonResponse(
                {"Message": "Closet does not exist"},
                status=400
            )
        outfit = Outfit.objects.create(**content)
        return JsonResponse(
            {"Outfit Created": outfit},
            encoder=OutfitEncoder,
            safe=False
        )