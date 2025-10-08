from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def mobile_check(mobile):
    if not mobile:
        raise ValidationError("Please enter mobile number")

class OrdersSerializer(serializers.Serializer):

    order_id = serializers.IntegerField()
    product_id = serializers.IntegerField(allow_null=False, required=True, min_value=1, max_value=999999)
    first_name = serializers.CharField(max_length=100, allow_null=False,  required=True)
    last_name = serializers.CharField(max_length=100, allow_null=False,  required=True)
    address = serializers.CharField(max_length=100, allow_null=False,  required=True)
    pincode = serializers.CharField(max_length=10, allow_null=False,  required=True)
    city = serializers.CharField(max_length=100, allow_null=False,  required=True)
    state = serializers.CharField(max_length=100, allow_null=False,  required=True)
    country = serializers.CharField(max_length=100, default='IND')
    email = serializers.EmailField(allow_null=False,  required=True)
    mobile = serializers.CharField(max_length=13, allow_null=False,  required=True,
                                   validators=[mobile_check])

    # Field Level Validation
    def validate_mobile(self, value):
        if not str(value).startswith('+91'):
            raise serializers.ValidationError("Mobile number should start with '+91'")
        return value

    # Object Level Validation
    def validate(self, data):
      address = data.get('address')
      pincode = data.get('pincode')
      city = data.get('city')
      state = data.get('state')
      mobile = data.get('mobile')

      if address and not (pincode or city or state or mobile):
          raise serializers.ValidationError("YOU HAVE ENTERED ADDRESS PLEASE ALSO ENTER PINCODE, CITY, STATE AND MOBILE")

      if len(str(pincode)) != 6 :
          raise serializers.ValidationError("Please enter valid pincode")

      return data



class AddOrderDetailsSerializer(serializers.Serializer):

    product_id = serializers.IntegerField(allow_null=False, required=True, min_value=1, max_value=999999)
    first_name = serializers.CharField(max_length=100, allow_null=False, required=True)
    last_name = serializers.CharField(max_length=100, allow_null=False, required=True)
    address = serializers.CharField(max_length=100, allow_null=False, required=True)
    pincode = serializers.CharField(max_length=10, allow_null=False, required=True)
    city = serializers.CharField(max_length=100, allow_null=False, required=True)
    state = serializers.CharField(max_length=100, allow_null=False, required=True)
    country = serializers.CharField(max_length=100, default='IND')
    email = serializers.EmailField(allow_null=False, required=True)
    mobile = serializers.CharField(max_length=13, allow_null=False, required=True,
                                   validators=[mobile_check])

    # Field Level Validation
    def validate_mobile(self, value):
        if not str(value).startswith('+91'):
            raise serializers.ValidationError("Mobile number should start with '+91'")
        return value

    # Object Level Validation
    def validate(self, data):
        address = data.get('address')
        pincode = data.get('pincode')
        city = data.get('city')
        state = data.get('state')
        mobile = data.get('mobile')

        if address and not (pincode or city or state or mobile):
            raise serializers.ValidationError(
                "YOU HAVE ENTERED ADDRESS PLEASE ALSO ENTER PINCODE, CITY, STATE AND MOBILE")

        if len(str(pincode)) != 6:
            raise serializers.ValidationError("Please enter valid pincode")

        return data