from django.urls import path
from .views import calculate_pricing

urlpatterns = [
    path('calculate_pricing/', calculate_pricing, name='calculate_pricing'),
]