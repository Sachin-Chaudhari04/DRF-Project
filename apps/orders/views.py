import datetime
from django.core.mail import send_mail
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OrderDetails
from .serializers import OrdersSerializer, AddOrderDetailsSerializer


# Create your views here.
@swagger_auto_schema(method='get', tags=['Orders'])
@api_view(['GET'])
def orders(request):
    orders = OrderDetails.objects.all().order_by('-order_id')
    serialize_data = OrdersSerializer(orders, many=True)
    return Response({"data": serialize_data.data})

@swagger_auto_schema(method='post', tags=['Orders'], request_body=AddOrderDetailsSerializer)
@api_view(['POST'])
def add_orders(request):
    serialized_data = AddOrderDetailsSerializer(data=request.data)
    serialized_data.is_valid(raise_exception=True)

    # Fetch fields from serialized data
    product_id = serialized_data.validated_data.get('product_id')
    first_name = serialized_data.validated_data.get('first_name')
    last_name = serialized_data.validated_data.get('last_name')
    address = serialized_data.validated_data.get('address')
    pincode = serialized_data.validated_data.get('pincode')
    city = serialized_data.validated_data.get('city')
    state = serialized_data.validated_data.get('state')
    country = serialized_data.validated_data.get('country')
    email = serialized_data.validated_data.get('email')
    mobile = serialized_data.validated_data.get('mobile')

    # Write ORM Query to save data
    order_placed = OrderDetails.objects.create(
        product_id=product_id,
        first_name=first_name,
        last_name=last_name,
        address=address,
        pincode=pincode,
        city=city,
        state=state,
        country=country,
        email=email,
        mobile=mobile
    )
    from django.core.mail import send_mail

    # Send Email
    if order_placed:
        message= f"""
                    Hello {order_placed.first_name} {order_placed.last_name}!,
                    
                    Thank you for your order!
                    
                    Your order has been successfully placed.
                    
                    🧾 Order Details:
                    - Order ID: {order_placed.order_id}
                    - Total Amount: ₹100
                    - Payment Method: UPI
                    - Order Date: {datetime.datetime.today()}
                    
                    📦 Shipping To:
                    {order_placed.first_name} {order_placed.last_name}
                    {order_placed.address}
                    {order_placed.pincode}
                    
                    We'll notify you once your order is shipped.
                    
                    Thank you for shopping with us!
                    Best Regards,
                    Sachin Chaudhari Pvt. Ltd. Pune
                    """

        send_mail(
            subject = f"Order Confirmation - Order #{order_placed.order_id}",
            message = message,
            from_email = "chaudharisachin1441@gmail.com",
            recipient_list = [order_placed.email],
            fail_silently=False
        )
    return Response({"Message" : "Your order has been placed successfully"})

@swagger_auto_schema(method='put', tags=['Orders'], request_body=AddOrderDetailsSerializer)
@api_view(['PUT'])
def update_orders(request, id):
    serialized_data = AddOrderDetailsSerializer(data=request.data)
    serialized_data.is_valid(raise_exception=True)

    # Fetch fields from serialized data
    product_id = serialized_data.validated_data.get('product_id')
    first_name = serialized_data.validated_data.get('first_name')
    last_name = serialized_data.validated_data.get('last_name')
    address = serialized_data.validated_data.get('address')
    pincode = serialized_data.validated_data.get('pincode')
    city = serialized_data.validated_data.get('city')
    state = serialized_data.validated_data.get('state')
    country = serialized_data.validated_data.get('country')
    email = serialized_data.validated_data.get('email')
    mobile = serialized_data.validated_data.get('mobile')

    # Write ORM Query to save data
    OrderDetails.objects.filter(order_id=id).update(
        product_id=product_id,
        first_name=first_name,
        last_name=last_name,
        address=address,
        pincode=pincode,
        city=city,
        state=state,
        country=country,
        email=email,
        mobile=mobile
    )
    return Response({"Message" : "Your order has been updated successfully"})

@swagger_auto_schema(method='delete', tags=['Orders'])
@api_view(['DELETE'])
def delete_orders(request, id):
    OrderDetails.objects.filter(order_id=id).delete()
    return Response({"Message" : "Your order has been deleted successfully"})

