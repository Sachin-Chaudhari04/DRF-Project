from django.urls import path
from . import views


urlpatterns = [
    path("api/v1/myorders", views.orders),
    path("api/v1/add_orders", views.add_orders),
    path("api/v1/update_orders/<int:id>", views.update_orders),
    path("api/v1/delete_orders/<int:id>", views.delete_orders),
]