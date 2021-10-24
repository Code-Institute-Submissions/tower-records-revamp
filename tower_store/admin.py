from django.contrib import admin
from .models import storeCategory, storeProduct

@admin.register(storeCategory)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['categoryName', 'slug']
    prepopulated_fields = {'slug': ('categoryName',)}


@admin.register(storeProduct)
class productAdmin(admin.ModelAdmin):
    list_display = ['productTitle', 'author', 'slug', 'productPrice', 'in_stock', 'createdOn', 'updatedOn']
    list_filter = ['in_stock', 'active']
    list_editable = ['productPrice', 'in_stock']
    prepopulated_fields = {'slug': ('productTitle',)}