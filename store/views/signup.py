from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #validation
        values = {
            'first_name':first_name,'last_name':last_name,'phone':phone,'email':email
              }
        error_message = None
        customer = Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        error_message = self.validateCustomer(customer)
        #saving



        if not error_message:
            print(first_name,last_name,phone,email,password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
             data = {
                 'error':error_message,'values':values
                 }
             return render(request,'signup.html',data)

        #return registerUser(request)
    def validateCustomer(self,customer):
        error_message = None
        if(not customer.first_name ):
            error_message = "First Name Required !!!"
        elif len(customer.first_name) < 6:
            error_message = "first name must be 6 char long"
        elif not customer.last_name:
            error_message = "Last Name is required"
        elif len(customer.last_name) < 4:
            error_message = "Last name must be more than 4 characters long"
        elif not customer.phone:
            error_message = "Phone Numer required"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 characters long"
        elif len(customer.password) < 6:
            error_message = "Password must be 7 characters long"
        elif len(customer.email) < 5:
            error_message = "Email must be 5 characters long"

        elif customer.isExists():
            error_message = 'Email Address already registered'
        return error_message

    
