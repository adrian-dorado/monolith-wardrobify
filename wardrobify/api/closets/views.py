from http.client import responses
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

# from common.encoders import OutfitsEncoder, ClosetsEncoder
# from .models import Closet, Outfit

# # Create your views here.

# # ---------------- CLOSET VIEWS -----------------


# @require_http_methods(["GET", "POST"])
# def closet_list(request):
#     if request.method == "GET":
#         closets = Closet.objects.all()
#         return JsonResponse({"Closets": closets}, encoder=ClosetsEncoder)
#     else:
#         content = json.loads(request.body)
#         closet = Closet.objects.create(**content)
#         return JsonResponse({"Closet": closet}, encoder=ClosetsEncoder, safe=False)


# @require_http_methods(["DELETE", "GET", "PUT"])
# def closet_details(request, pk):
#     if request.method == "GET":
#         try:
#             closet = Closet.objects.get(id=pk)
#             return JsonResponse({"Closet": closet}, encoder=ClosetsEncoder, safe=False)
#         except Closet.DoesNotExist:
#             response = JsonResponse({"Message": "Closet does not exist."})
#             response.status_code = 404
#             return response
#     elif request.method == "DELETE":
#         try:
#             closet = Closet.objects.get(id=pk)
#             closet.delete()
#             return JsonResponse(
#                 {"Closet Deleted": closet}, encoder=ClosetsEncoder, safe=False
#             )
#         except Closet.DoesNotExist:
#             response = JsonResponse({"Message": "Closet does not exist."})
#             response.status_code = 404
#             return response
#     else:  # PUT
#         try:
#             content = json.loads(request.body)
#             closet = Closet.objects.filter(id=pk).update(**content)
#             return JsonResponse(
#                 {"Closet Updated": closet}, encoder=ClosetsEncoder, safe=False
#             )
#         except Closet.DoesNotExist:
#             response = JsonResponse({"Message": "Closet does not exist."})
#             response.status_code = 404
#             return response


# # ---------------- OUTFIT VIEWS ------------------


# @require_http_methods(["GET", "POST"])
# def outfit_list(request):
#     if request.method == "GET":
#         outfits = Outfit.objects.all()
#         return JsonResponse({"Outfits": outfits}, encoder=OutfitsEncoder)
#     else:
#         try:
#             closet_name = content["name"]
#             closet = Closet.objects.get(name=closet_name)
#             content["name"] = closet
#         except Closet.DoesNotExist:
#             response = JsonResponse({"Message": "Closet does not exist."})
#             response.status_code = 404
#             return response
#         content = json.loads(request.body)
#         outfit = Outfit.objects.create(**content)
#         return JsonResponse({"Outfits": outfit}, encoder=OutfitsEncoder, safe=False)


# @require_http_methods(["DELETE", "GET", "PUT"])
# def outfit_details(request, pk):
#     if request.method == "GET":
#         try:
#             outfit = Outfit.objects.get(id=pk)
#             return JsonResponse({"Outfit": outfit}, encoder=OutfitsEncoder, safe=False)
#         except Closet.DoesNotExist:
#             response = JsonResponse({"Message": "Outfit does not exist."})
#             response.status_code = 404
#             return response
#     elif request.method == "DELETE":
#         try:
#             outfit = Outfit.objects.get(id=pk)
#             outfit.delete()
#             return JsonResponse(
#                 {"Outfit Deleted": outfit}, encoder=OutfitsEncoder, safe=False
#             )
#         except Outfit.DoesNotExist:
#             response = JsonResponse({"Message": "Outfit does not exist."})
#             response.status_code = 404
#             return response
#     else:  # PUT
#         try:
#             closet_name = content["name"]
#             closet = Closet.objects.get(name=closet_name)
#             content["name"] = closet
#         except Closet.DoesNotExist:
#             response = JsonResponse({"Message": "Closet does not exist."})
#             response.status_code = 404
#             return response
#         try:
#             content = json.loads(request.body)
#             outfit = Outfit.objects.filter(id=pk).update(**content)
#             return JsonResponse(
#                 {"Outfit Updated": outfit}, encoder=OutfitsEncoder, safe=False
#             )
#         except Outfit.DoesNotExist:
#             response = JsonResponse({"Message": "Outfit does not exist."})
#             response.status_code = 404
#             return response