from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from django.core import serializers

# Create your views here.
def pivot(request):
    return render(request, 'dashboard/pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)