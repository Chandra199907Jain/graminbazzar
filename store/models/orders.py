from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    def __str__(self):
        return self.address
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length = 1000,default = 0000000000000000)
    phone = models.CharField(max_length = 10,default = 0000000000)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default = False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer = customer_id)\
            .order_by('-date')
            