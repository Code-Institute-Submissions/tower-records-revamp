from django.urls import path

from . import views

app_name = 'tower_store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.more_detail, name='more_detail'),
]
