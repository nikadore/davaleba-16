from django.db import models

class Product(models.Model):
    name = models.CharField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
