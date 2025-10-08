from itertools import product

from django.db import models


# Create your models here.

class ProductDetails(models.Model):

    product_id = models.AutoField(null=False, primary_key=True)
    sku = models.CharField(null=True, max_length=100, unique=True, blank=False)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_price = models.FloatField(null=False, blank=False)
    product_stock = models.IntegerField(null=False, blank=False)


    def __str__(self):
        return f"{self.product_id}_{self.product_name}"

    class Meta:
        verbose_name = "Product Detail"
        verbose_name_plural = "Product Details"
