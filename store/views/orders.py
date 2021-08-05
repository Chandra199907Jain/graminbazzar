from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from django.views import View


class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request,'orders.html',{'orders':orders})
   
    