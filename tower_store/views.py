from django.shortcuts import render

from .models import storeCategory, storeProduct

def categories(request):
    return {
        'categories': storeCategory.objects.all()
    }

def all_products(request):
    products = storeProduct.objects.all()
    return render(request, 'storeapp/main.html', {'products': products})