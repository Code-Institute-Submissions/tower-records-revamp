# Generated by Django 3.2.8 on 2021-10-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tower_store', '0002_alter_storeproduct_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
