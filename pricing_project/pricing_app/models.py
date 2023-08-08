# pricing_app/models.py

from django.db import models
from django.contrib.auth.models import User


class PricingConfiguration(models.Model):
    name = models.CharField(max_length=100)
    distance_base_price = models.DecimalField(max_digits=6, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=6, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=6, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=6, decimal_places=2)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.name


class PricingLog(models.Model):
    configuration = models.ForeignKey(PricingConfiguration, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.configuration} - {self.action} - {self.timestamp}"
