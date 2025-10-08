from django.db import models

# Create your models here.

class OrderDetails(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='IND', null=True)
    email = models.EmailField()
    mobile = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Order Detail"
        verbose_name_plural = "Order Details"