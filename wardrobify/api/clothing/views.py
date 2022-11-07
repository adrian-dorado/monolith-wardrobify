from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.encoders import CategoryEncoder, ItemCategoryEncoder, OutfitEncoder, OutfitItemEncoder
from .models import *

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
        try:
            content = json.loads(request.body)
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


# ------------------- Item Category VIEWS --------------------


@require_http_methods(["GET", "POST"])
def list_item_categories(request):
    if request.method == "GET":
        item_categories = ItemCategory.objects.all()
        return JsonResponse({"Item Categories": item_categories}, encoder=ItemCategoryEncoder)
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
        item_category = ItemCategory.objects.create(**content)
        return JsonResponse({"Item Category": item_category}, encoder=ItemCategoryEncoder, safe=False)


@require_http_methods(["GET", "PUT", "DELETE"])
def item_category_details(request, pk):
    if request.method == "GET":
        try:
            item_category = ItemCategory.objects.get(id=pk)
            return JsonResponse({"Item Category": item_category}, encoder=ItemCategoryEncoder, safe=False)
        except ItemCategory.DoesNotExist:
            response = JsonResponse({"Message": "Item Category Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "PUT":
        try:
            category_name = content["name"]
            category = Category.objects.get(name=category_name)
            content["name"] = category
        except Category.DoesNotExist:
            return JsonResponse(
                {"Message": "Invalid ID"},
                status=400,
            )
        try:
            content = json.loads(request.body)
            item_category = ItemCategory.objects.filter(id=pk).update(**content)
            return JsonResponse({"Item Category Updated": item_category}, encoder=ItemCategoryEncoder, safe=False)
        except ItemCategory.DoesNotExist:
            response = JsonResponse({"Message": "Item Category Does Not Exist"})
            response.status_code = 404
            return response
    else:
        try:
            item_category = ItemCategory.objects.get(id=pk)
            item_category.delete()
            return JsonResponse({"Category Deleted": item_category}, encoder=ItemCategoryEncoder, safe=False)
        except ItemCategory.DoesNotExist:
            response = JsonResponse({"Message": "Category does not exist"})
            response.status_code = 404
            return response
    