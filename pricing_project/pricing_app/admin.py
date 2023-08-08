from django import forms
from django.contrib import admin
from .models import PricingConfiguration, PricingLog


class PricingConfigurationAdminForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = '__all__'


class PricingConfigurationAdmin(admin.ModelAdmin):
    form = PricingConfigurationAdminForm
    list_display = ('name', 'distance_base_price', 'distance_additional_price', 'time_multiplier_factor', 'waiting_charges', 'enabled')
    list_filter = ('enabled',)
    search_fields = ('name', 'created_by__username')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        PricingLog.objects.create(configuration=obj, action='Created' if not change else 'Updated', user=request.user)


admin.site.register(PricingConfiguration, PricingConfigurationAdmin)
admin.site.register(PricingLog)