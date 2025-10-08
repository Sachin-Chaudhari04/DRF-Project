from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@swagger_auto_schema(method='get', tags=['Reviews'])
@api_view(['GET'])
def review_lists(request):
    data = Review.objects.all()
    serializer = ReviewSerializer(data, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='post', tags=['Reviews'], request_body=ReviewSerializer)
@api_view(['POST'])
def add_review(request):
    data = ReviewSerializer(data=request.data)
    data.is_valid(raise_exception=True)

    Review.objects.create(product=data.validated_data.get('product'),
                          rating=data.validated_data.get('rating'),
                          comment=data.validated_data.get('comment'),
                          created_at=data.validated_data.get('created_at'),
                          updated_at=data.validated_data.get('updated_at')
                          )

    return Response({"message": "Your Valuable Review Has Successfully Added!"})


@swagger_auto_schema(method='put', tags=['Reviews'], request_body=ReviewSerializer)
@api_view(['PUT'])
def update(request, id):
    data = ReviewSerializer(data=request.data)
    data.is_valid(raise_exception=True)

    Review.objects.filter(id=id).update(
        product=data.validated_data.get('product'),
        rating=data.validated_data.get('rating'),
        comment=data.validated_data.get('comment'),
        created_at=data.validated_data.get('created_at'),
        updated_at=data.validated_data.get('updated_at')
    )

    return Response({"message": "Your Review Has Successfully Updated!"})

@swagger_auto_schema(method='delete', tags=['Reviews'])
@api_view(['DELETE'])
def delete(request, id):
    Review.objects.get(id=id).delete()

    return Response({"message": "Your Review Has Successfully Deleted!"})