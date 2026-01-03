from django.shortcuts import render
from django.db.models import Q, F
from .models import Product

product_1 = Product.objects.filter(Q(price__gt = 50) | Q(quantity__lt = 10))
product_2 = Product.objects.filter(Q(name__icontains = 'phone') & Q(price__range = (100, 500)))
product_3 = Product.objects.filter(~Q(price__lt = 200))

product_4 = Product.objects.filter(price = F('price') + 10)
product_5 = Product.objects.filter(price__gt = F('quantity'))
product_6 = Product.objects.filter(quantity = F('quantity') + 1)





