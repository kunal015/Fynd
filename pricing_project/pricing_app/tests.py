from django.test import TestCase
from .utils import calculate_pricing
from .forms import PricingConfigurationForm

class PricingTestCase(TestCase):
    def test_pricing_calculation(self):
        # Test the pricing calculation function
        dbp = 80.00
        dap = 30.00
        tmf = 1.25
        wc = 5.00
        total_distance = 4.5
        time_duration = 1.5
        waiting_time= 2
        total_cost = calculate_pricing(dbp, dap, tmf, wc, total_distance, time_duration, waiting_time)
        self.assertAlmostEqual(total_cost, 126.875, places=2)

    def test_pricing_form_validation(self):
        # Test form validation
        form_data = {
            'distance_base_price': 80.00,
            'distance_additional_price': 30.00,
            'time_multiplier_factor': 1.25,
            'waiting_charges': 5.00,
            'total_distance': 4.5,
            'time_duration': 1.5,
            'waiting_time': 2
        }
        form = PricingConfigurationForm(data=form_data)
        self.assertTrue(form.is_valid())