from http.client import responses

from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from .models import ProductDetails
from rest_framework.response import Response
from .serializers import ProductDetailsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@swagger_auto_schema(method='get', tags=['Products'])
@api_view(['GET'])
def listing(request):
    details_data = ProductDetails.objects.all()
    serialize = ProductDetailsSerializer(details_data, many=True)

    return Response(serialize.data)


@swagger_auto_schema(method='post', tags=['Products'], request_body=ProductDetailsSerializer)
@api_view(['POST'])
def add_product(request):
    products = ProductDetailsSerializer(data=request.data)
    products.is_valid(raise_exception=True)

    # Fetch fields from serialized data(products)
    ProductDetails.objects.create(
        product_name=products.validated_data.get('product_name'),
        product_price=products.validated_data.get('product_price'),
        product_stock=products.validated_data.get('product_stock')
    )

    return Response({"message": "Your Product Successfully Added"})


@swagger_auto_schema(method='put', tags=['Products'], request_body=ProductDetailsSerializer)
@api_view(['PUT'])
def update_product(request, id):
    data = ProductDetailsSerializer(data=request.data)
    data.is_valid(raise_exception=True)

    ProductDetails.objects.filter(product_id=id).update(
        product_name=data.validated_data.get('product_name'),
        product_price=data.validated_data.get('product_price'),
        product_stock=data.validated_data.get('product_stock')
    )
    return Response({"message": "Your Product Successfully Updated"})


@swagger_auto_schema(method='delete', tags=['Products'])
@api_view(['DELETE'])
def delete_product(request, id):
    ProductDetails.objects.filter(product_id=id).delete()
    return Response({"message": "Your Product Successfully Deleted"})
