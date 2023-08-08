from django import forms
from .models import PricingConfiguration

class PricingConfigurationForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = ['distance_base_price', 'distance_additional_price', 'time_multiplier_factor', 'waiting_charges']