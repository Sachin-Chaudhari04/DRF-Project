from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/reviewslist/", views.review_lists),
    path("api/v1/addreviews/", views.add_review),
    path("api/v1/update/<int:id>", views.update),
    path("api/v1/delete/<int:id>", views.delete),
]
