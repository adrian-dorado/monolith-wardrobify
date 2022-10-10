from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.encoders import OutfitsEncoder, ClosetsEncoder
from .models import Closet, Outfit

# Create your views here.

# ---------------- CLOSET VIEWS -----------------

@require_http_methods(["GET", "POST"])
def closet_list(request):
    if request.method == "GET":
        closets = Closet.objects.all()
        return JsonResponse({"Closets": closets}, encoder=ClosetsEncoder)
    else:
        content = json.loads(request.body)
        closet = Closet.objects.create(**content)
        return JsonResponse({"Closet": closet}, encoder=ClosetsEncoder, safe=False)


# @require_http_methods(["DELETE", "GET", "PUT"])
# def closet_details(request, pk):
#     if request.method == "GET":
#         try:
