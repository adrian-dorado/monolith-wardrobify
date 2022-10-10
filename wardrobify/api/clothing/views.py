from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.encoders import (
    TopEncoder,
    BottomEncoder,
    UndergarmentEncoder,
    FootwearEncoder,
    AccessoriesEncoder,
)

from .models import (
    Top,
    Bottom,
    Undergarment,
    Footwear,
    Accessorie,
)

# ------------------- TOP VIEWS --------------------


@require_http_methods(["GET", "POST"])
def list_tops(request):
    if request.method == "GET":
        tops = Top.objects.all()
        return JsonResponse({"Tops": tops}, encoder=TopEncoder)
    else:
        content = json.loads(request.body)
        top = Top.objects.create(**content)
        return JsonResponse({"Top Created": top}, encoder=TopEncoder, safe=False)


@require_http_methods(["DELETE", "GET", "PUT"])
def top_details(request, pk):
    if request.method == "GET":
        try:
            top = Top.objects.get(id=pk)
            return JsonResponse({"Top Details": top}, encoder=TopEncoder, safe=False)
        except Top.DoesNotExist:
            response = JsonResponse({"Message": "Top Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            top = Top.objects.get(id=pk)
            top.delete()
            return JsonResponse({"Top Deleted": top}, encoder=TopEncoder, safe=False)
        except Top.DoesNotExist:
            response = JsonResponse({"Message": "Top Does Not Exist"})
            response.status_code = 404
            return response
    else:  # PUT
        try:
            content = json.loads(request.body)
            top = Top.objects.get(id=pk)
            properties = ["name", "brand", "top_type"]
            for prop in properties:
                if prop in content:
                    setattr(top, properties, content[properties])
            top.save()
            return JsonResponse({"Top Updated": top}, encoder=TopEncoder, safe=False)
        except Top.DoesNotExist:
            response = JsonResponse({"Message": "Top Does Not Exist"})
            response.status_code = 404
            return response


# ----------------- BOTTOM VIEWS -------------------


@require_http_methods(["GET", "POST"])
def list_bottoms(request):
    if request.method == "GET":
        bottoms = Bottom.objects.all()
        return JsonResponse({"Bottoms": bottoms}, encoder=BottomEncoder)
    else:
        content = json.loads(request.body)
        bottom = Bottom.objects.create(**content)
        return JsonResponse(
            {"Bottoms Created": bottom}, encoder=BottomEncoder, safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def bottom_details(request, pk):
    if request.method == "GET":
        try:
            bottom = Bottom.objects.get(id=pk)
            return JsonResponse(
                {"Bottom Details": bottom}, encoder=BottomEncoder, safe=False
            )
        except Top.DoesNotExist:
            response = JsonResponse({"Message": "Bottom Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            bottom = Bottom.objects.get(id=pk)
            bottom.delete()
            return JsonResponse(
                {"Bottom Deleted": bottom}, encoder=BottomEncoder, safe=False
            )
        except Top.DoesNotExist:
            response = JsonResponse({"Message": "Bottom Does Not Exist"})
            response.status_code = 404
            return response
    else:  # PUT
        try:
            content = json.loads(request.body)
            bottom = Bottom.objects.get(id=pk)
            properties = ["name", "brand", "bottom_type"]
            for prop in properties:
                if prop in content:
                    setattr(bottom, properties, content[properties])
            bottom.save()
            return JsonResponse(
                {"Bottom Updated": bottom}, encoder=BottomEncoder, safe=False
            )
        except Bottom.DoesNotExist:
            response = JsonResponse({"Message": "Bottom Does Not Exist"})
            response.status_code = 404
            return response


# ----------------- UNDERGARMENT VIEWS ------------------


@require_http_methods(["GET", "POST"])
def list_undergarments(request):
    if request.method == "GET":
        undergarments = Undergarment.objects.all()
        return JsonResponse(
            {"Undergarments": undergarments}, encoder=UndergarmentEncoder
        )
    else:
        content = json.loads(request.body)
        undergarment = Undergarment.objects.create(**content)
        return JsonResponse(
            {"Undergarment Created": undergarment},
            encoder=UndergarmentEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def undergarment_details(request, pk):
    if request.method == "GET":
        try:
            undergarment = Undergarment.objects.get(id=pk)
            return JsonResponse(
                {"Undergarment Details": undergarment},
                encoder=UndergarmentEncoder,
                safe=False,
            )
        except Undergarment.DoesNotExist:
            response = JsonResponse({"Message": "Undergarment Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            undergarment = Undergarment.objects.get(id=pk)
            undergarment.delete()
            return JsonResponse(
                {"Undergarment Deleted": Undergarment},
                encoder=UndergarmentEncoder,
                safe=False,
            )
        except Undergarment.DoesNotExist:
            response = JsonResponse({"Message": "Undergarment Does Not Exist"})
            response.status_code = 404
            return response
    else:  # PUT
        try:
            content = json.loads(request.body)
            undergarment = Undergarment.objects.get(id=pk)
            properties = ["name", "brand", "Undergarment_type"]
            for prop in properties:
                if prop in content:
                    setattr(undergarment, properties, content[properties])
            undergarment.save()
            return JsonResponse(
                {"Undergarment Updated": Undergarment},
                encoder=UndergarmentEncoder,
                safe=False,
            )
        except Undergarment.DoesNotExist:
            response = JsonResponse({"Message": "Undergarment Does Not Exist"})
            response.status_code = 404
            return response


# ----------------- FOOTWEAR VIEWS -------------------


@require_http_methods(["GET", "POST"])
def list_footwear(request):
    if request.method == "GET":
        all_footwear = Footwear.objects.all()
        return JsonResponse({"Footwear": all_footwear}, encoder=FootwearEncoder)
    else:
        content = json.loads(request.body)
        footwear = Footwear.objects.create(**content)
        return JsonResponse(
            {"Footwear Created": footwear}, encoder=FootwearEncoder, safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def footwear_details(request, pk):
    if request.method == "GET":
        try:
            footwear = footwear.objects.get(id=pk)
            return JsonResponse(
                {"Footwear Details": footwear}, encoder=FootwearEncoder, safe=False
            )
        except Footwear.DoesNotExist:
            response = JsonResponse({"Message": "Footwear Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            footwear = footwear.objects.get(id=pk)
            footwear.delete()
            return JsonResponse(
                {"Footwear Deleted": footwear}, encoder=FootwearEncoder, safe=False
            )
        except Footwear.DoesNotExist:
            response = JsonResponse({"Message": "Footwear Does Not Exist"})
            response.status_code = 404
            return response
    else:  # PUT
        try:
            content = json.loads(request.body)
            footwear = footwear.objects.get(id=pk)
            properties = ["name", "brand", "footwear_type"]
            for prop in properties:
                if prop in content:
                    setattr(footwear, properties, content[properties])
            footwear.save()
            return JsonResponse(
                {"Footwear Updated": footwear}, encoder=FootwearEncoder, safe=False
            )
        except Footwear.DoesNotExist:
            response = JsonResponse({"Message": "Footwear Does Not Exist"})
            response.status_code = 404
            return response


# ----------------- ACCESSORIES VIEWS ------------------


@require_http_methods(["GET", "POST"])
def list_accessories(request):
    if request.method == "GET":
        accessories = Accessorie.objects.all()
        return JsonResponse(
            {"Accessories": accessories},
            encoder=AccessoriesEncoder,
        )
    else:
        content = json.loads(request.body)
        accessory = Accessorie.objects.create(**content)
        return JsonResponse(
            {"Accessory Created": accessory}, encoder=AccessoriesEncoder, safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def accessory_details(request, pk):
    if request.method == "GET":
        try:
            accessory = Accessorie.objects.get(id=pk)
            return JsonResponse(
                {"Accessory Details": accessory}, encoder=AccessoriesEncoder, safe=False
            )
        except Accessorie.DoesNotExist:
            response = JsonResponse({"Message": "Accessory Does Not Exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            accessory = Accessorie.objects.get(id=pk)
            accessory.delete()
            return JsonResponse(
                {"Accessory Deleted": accessory}, encoder=AccessoriesEncoder, safe=False
            )
        except Accessorie.DoesNotExist:
            response = JsonResponse({"Message": "Accessory Does Not Exist"})
            response.status_code = 404
            return response
    else:  # PUT
        try:
            content = json.loads(request.body)
            accessory = Accessorie.objects.get(id=pk)
            properties = ["name", "brand", "accessorie_type"]
            for prop in properties:
                if prop in content:
                    setattr(accessory, properties, content[properties])
            accessory.save()
            return JsonResponse(
                {"Accessory Updated": accessory}, encoder=AccessoriesEncoder, safe=False
            )
        except Accessorie.DoesNotExist:
            response = JsonResponse({"Message": "Accessory Does Not Exist"})
            response.status_code = 404
            return response
