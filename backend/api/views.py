from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
import json


@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    "DRF API"
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data = model_to_dict(model_data, fields=['id', 'title', 'content', 'sale_price'])
    #     data = ProductSerializer(instance).data

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        print(data)
        return Response(data)
