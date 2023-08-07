
from django.urls import path ,include
from .views import product_details, view_products

urlpatterns = [
    path('<int:id>', product_details),
    path('', view_products),
]
