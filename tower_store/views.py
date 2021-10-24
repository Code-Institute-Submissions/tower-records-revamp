from django.shortcuts import render

from .models import storeCategory, storeProduct

def all_products(request):
    products = storeProduct.objects.all()
    return render(request, 'storeapp/main.html', {'products': products})