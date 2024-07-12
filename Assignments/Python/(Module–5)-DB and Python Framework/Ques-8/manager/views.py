from django.shortcuts import render,redirect
from .models import Manager
from django.contrib import messages
from master.models import ProductSubCategory
from .forms import ProductForm,CompanyForm
from functools import wraps

from django.core.paginator import Paginator

# Create your views here.

def login_required(function):
    @wraps(function)
    def wrapped_view(request,*args,**kwargs):
        if request.COOKIES.get('manager_id') and request.COOKIES.get('manager_name'):
            return function(request,*args,**kwargs)
        else:
            return redirect("manager_login_view")
    return wrapped_view


def manager_login_view(request):
    if request.method == 'POST':
        manager_id_ = request.POST.get('manager_id')
        password_ = request.POST.get('password')
        try:
            manager_queryset = Manager.objects.get(manager_id = manager_id_)
            if manager_queryset.password == password_:
                response = redirect('manager_dashboard_view')
                response.set_cookie('manager_id',manager_id_)
                response.set_cookie('manager_name',f'{manager_queryset.first_name} {manager_queryset.last_name}')
                messages.success(request,"Login Successfull")
                return response
            else:
                messages.error(request,"Manager ID or Password Does Not Matches!!")
                return redirect('manager_login_view')
        except Manager.DoesNotExist:
            messages.error(request,"Manager Not Found")
            return redirect('manager_login_view')
    return render(request,"manager/manager_login.html")


@login_required
def manager_dashboard_view(request):
    products_queryset = ProductSubCategory.objects.all()
    
    if request.GET.get('search'):
        products_queryset = products_queryset.filter(
        company__name__icontains=request.GET.get('search')
    ) | products_queryset.filter(
        model_name__icontains=request.GET.get('search')
    ) | products_queryset.filter(
        ram__icontains=request.GET.get('search')
    ) | products_queryset.filter(
        price__icontains=request.GET.get('search')
    )
    # for pagination
    page = request.GET.get('page',1)
    paginator = Paginator(products_queryset,3) # this show only 4 records
    try:
        products_queryset = paginator.page(page)
    except Exception as e:
        messages.error(request,e)

    product_form = ProductForm()
    company_form = CompanyForm()

    if request.method == "POST":
        product_form = ProductForm(request.POST,request.FILES)
        company_form = CompanyForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request,"Product added successfully.")
            return redirect("manager_dashboard_view")
        elif company_form.is_valid():
            company_form.save()
            messages.success(request,"Company Name added successfully.")
            return redirect("manager_dashboard_view")
        else:
            messages.error(request,"Something Went Wrong")
            return redirect("manager_dashboard_view")
        
    context = {
        'products' : products_queryset,
        'product_form' : product_form,
        'company_form' : company_form,
    }

    return render(request,"manager/manager_dashboard.html",context)


@login_required
def manager_product_edit(request,id):
    data = ProductSubCategory.objects.get(id=id)
    if request.method == "POST":
        model_name_ = request.POST.get('model_name')
        image_ = request.FILES.get('image')
        ram_ = request.POST.get('ram')
        price_ = request.POST.get('price')
        if model_name_:
            data.model_name = model_name_

        if image_:
            data.image = image_

        if ram_:
            data.ram = ram_

        if price_:
            data.price = price_
        data.save()
        messages.success(request,"Product Edit Successfully")
        return redirect("manager_dashboard_view")
    else:
        messages.error(request,"Somthing Went Wrong")
        return redirect("manager_dashboard_view")
    
    
@login_required
def manager_product_delete(request,id):
    product = ProductSubCategory.objects.get(basemodel_ptr_id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request,"Product Delete Successfully")
        return redirect("manager_dashboard_view")

def manager_logout_view(request):
    response = redirect("manager_login_view")
    response.delete_cookie('manager_id')
    response.delete_cookie('manager_name')
    messages.success(request,'You Are Looged Out')
    return response
