import datetime

from django.db import models


class Product(models.Model):
    product_id: int = models.AutoField(primary_key=True)
    image = models.ImageField("image",blank=True,upload_to='media')
    product_name:str = models.CharField('product_name',max_length=255)
    sell = models.IntegerField('Цена',default= 0)

class Order(models.Model):
    full_name:str = models.CharField('name',max_length=255)
    phone_number: str = models.CharField('phone',max_length=15)