from django.http import response
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from tower_store.models import storeProduct

from tower_store.models import storeProduct
from .shopping_basket import Basket

def basket_summary(request):
    return render(request, 'storeapp/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(storeProduct, id=product_id)
        basket.add(product=product)
        response = JsonResponse({'test':'data'})
        return response