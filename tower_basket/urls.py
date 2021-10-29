from django.urls import path

from . import views

app_name = 'tower_basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
]
