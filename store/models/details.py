from django.db import models
from .product import Product
from .customer import Customer
from .orders import Order

class Details(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    orders = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    


   