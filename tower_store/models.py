from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class storeCategory(models.Model):
    categoryName = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    

    def __str__(self):
        return self.categoryName


class storeProduct(models.Model):
    category = models.ForeignKey(storeCategory, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    productTitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Tower Records Admin')
    productDescription = models.TextField(blank=True)
    images = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    productPrice = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-createdOn',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    def __str__(self):
        return self.productTitle