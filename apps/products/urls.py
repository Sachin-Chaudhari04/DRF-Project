from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/listing", views.listing),
    path("api/v1/add_product", views.add_product),
    path("api/v1/update_product/<int:id>", views.update_product),
    path("api/v1/delete_product/<int:id>", views.delete_product),

    ]