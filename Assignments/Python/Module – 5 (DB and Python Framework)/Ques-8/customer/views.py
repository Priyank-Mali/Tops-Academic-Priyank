from django.shortcuts import render,redirect
from functools import wraps
from .forms import CustomerRegistrationForm
from .models import Customer
from django.contrib import messages
from master.models import ProductSubCategory
from functools import wraps

# Create your views here.

def login_required(function):
    @wraps
    def wrapped_function(request,*args,**kwargs):
        if request.COOKIES.get('email') and request.COOKIES.get('customer_name'):
            return  function(request,*args,**kwargs)
        else:
            return redirect("customer_login_view")
    return wrapped_function


def customer_login_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        password_ = request.POST.get('password')
        try:
            customer_queryset = Customer.objects.get(email = email_)
            if customer_queryset.password == password_:
                response = redirect('customer_dashboard_view')
                response.set_cookie('email',email_)
                response.set_cookie('customer_name',f'{customer_queryset.first_name} {customer_queryset.last_name}')
                messages.success(request,"Login Successfull")
                return response
            else:
                messages.error(request,"Email or Password Does Not Matches!!")
                return redirect('customer_login_view')
        except Customer.DoesNotExist:
            messages.error(request,"Custoner Not Exists")
            return redirect('customer_login_view')
    return render(request,"customer/customer_login.html")


def customer_registration_view(request):
    form = CustomerRegistrationForm()
    context = {
        'customer_form' : form
    }
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Retistration Done.\n You password is you mobile number")
            return redirect("customer_login_view")
        else:
            messages.error(request,"something went wrong")
            return redirect("customer_registration_view")
    return render(request,'customer/cutomer_registration.html',context)


# @login_required
def customer_dashboard_view(request):
    products_queryset = ProductSubCategory.objects.all()
    if request.GET.get('search'):
        products_queryset = products_queryset.filter(
            company__name__icontains = request.GET.get('search')
        ) |  products_queryset.filter(
            model_name__icontains = request.GET.get('search')
        ) | products_queryset.filter(
            ram__icontains=request.GET.get('search')
        ) | products_queryset.filter(
            price__icontains=request.GET.get('search')
        )
    context = {
        'products' : products_queryset
    }
    return render(request,"customer/customer_dashboard.html",context)
  

def customer_logout_view(request):
    response = redirect("customer_login_view")
    response.delete_cookie('email')
    response.delete_cookie('customer_name')
    messages.success(request,"You are Logged Out")
    return response