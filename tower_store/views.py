from django.shortcuts import get_object_or_404, render

from .models import storeCategory, storeProduct

def categories(request):
    return {
        'categories': storeCategory.objects.all()
    }

def all_products(request):
    products = storeProduct.objects.all()
    return render(request, 'storeapp/main.html', {'products': products})

def more_detail(request, slug):
    product = get_object_or_404(storeProduct, slug=slug, in_stock=True)
    return render(request, 'storeapp/products/moredetails.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(storeCategory, slug=category_slug)
    products = storeProduct.objects.filter(category=category)
    return render(request, 'storeapp/products/category.html', {'category': category, 'products': products})
