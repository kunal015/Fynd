from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PricingConfiguration
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@csrf_exempt 
def calculate_pricing(request):
    try:
        data = request.data
        distance = data.get('distance', 0)
        time = data.get('time', 0)

        config = PricingConfiguration.objects.filter(enabled=True).first()
        if not config:
            return Response({"error": "No active pricing configuration found."}, status=400)

        base_price = config.distance_base_price + (distance * config.distance_additional_price)
        time_multiplier = config.time_multiplier_factor
        if time > 60:
            time_multiplier = config.time_multiplier_factor * 2.2
        elif time > 30:
            time_multiplier = config.time_multiplier_factor * 1.25

        total_price = (base_price + time_multiplier) + (time / 3) * config.waiting_charges
        return Response({"price": total_price}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(('GET',))
def calculate_pricing(request):
    if request.method == 'GET':
        try:
            data = request.data
            distance = float(data.get('distance', 0))
            time = float(data.get('time', 0))
            print("Distance=", distance)
            config = PricingConfiguration.objects.filter(enabled=True).first()
            if not config:
                return Response({"error": "No active pricing configuration found."}, status=400)

            base_price = float(config.distance_base_price) + float(distance * float(config.distance_additional_price))
            time_multiplier = float(config.time_multiplier_factor)
            if time > 60:
                time_multiplier = float(config.time_multiplier_factor) * 2.2
            elif time > 30:
                time_multiplier = float(config.time_multiplier_factor) * 1.25

            total_price = (base_price + time_multiplier) + (time / 3) * float(config.waiting_charges)
            return Response({"price": total_price}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        return JsonResponse({'price': "400"})