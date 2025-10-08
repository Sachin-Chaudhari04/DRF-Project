from django.db import models

from ..products.models import ProductDetails

def validate_rating(rating):
    if rating not in (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5):
        raise ValueError('Invalid rating')

# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField(blank=False, null=False, validators=[validate_rating])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.product_name} Rating: {self.rating}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"




