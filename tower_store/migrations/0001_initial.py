# Generated by Django 3.2.8 on 2021-10-18 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='storeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='storeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productTitle', models.CharField(max_length=255)),
                ('author', models.CharField(default='Tower Records Admin', max_length=255)),
                ('productDescription', models.TextField(blank=True)),
                ('images', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=4)),
                ('in_stock', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='tower_store.storecategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-createdOn',),
            },
        ),
    ]
