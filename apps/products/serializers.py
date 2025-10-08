from rest_framework import serializers

class ProductDetailsSerializer(serializers.Serializer):

    product_name = serializers.CharField(max_length=100, allow_null=False, required=True)
    product_price = serializers.FloatField(allow_null=False, required=True)
    product_stock = serializers.IntegerField(allow_null=False, required=True)

