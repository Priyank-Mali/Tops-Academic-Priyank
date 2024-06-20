from django.shortcuts import render,redirect
from functools import wraps
from .models import Employee
from django.contrib import messages


# Create your views here.

"""
@wraps is a decorator from the functools module. 
It is used to preserve the original view function's metadata (such as its name and docstring) 
when it is wrapped by the login_required decorator.

The decorator checks if the employee_id and password cookies are set in the request. These cookies are presumably used to store the user's authentication information.

If both cookies are present (request.COOKIES.get("employee_id") and request.COOKIES.get("password")),
the decorator allows access to the original view function by calling view_func(request, *args, **kwargs).

If either cookie is missing, the user is not authenticated, and the decorator redirects them to the login view using redirect("employee_login_view").

Wrapper function that checks for authentication before calling the view.

Parameters:
    request (HttpRequest): The HTTP request object.
    *args: Additional positional arguments passed to the view.
    **kwargs: Additional keyword arguments passed to the view.

Returns:
    HttpResponse: The response object from the view function if authenticated,
                    or a redirect response to the login view if not authenticated.

"""
from functools import wraps
from django.shortcuts import redirect

def login_required(view_func):
    """
    Returns:
        function: The wrapped view function with added authentication check.
    """
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Check if 'employee_id' and 'employee_name' cookies are set in the request
        if request.COOKIES.get("employee_id") and request.COOKIES.get("employee_name") and request.COOKIES.get("password"):
            # If authenticated, call the original view function
            return view_func(request, *args, **kwargs)
        else:
            # If not authenticated, redirect to the login view
            return redirect("employee_login_view")
    
    # Return the wrapped view function
    return wrapped_view

# --------employee login view------------
def employee_login_view(request):
    if request.method=="POST":
        employee_id_ = request.POST["employee_id"]
        password_ = request.POST["password"]
        try:
            get_employee = Employee.objects.get(employee_id=employee_id_)
            if get_employee.password == password_:
                messages.success(request,f"Hello {get_employee.first_name} {get_employee.last_name},Now you are Logged In.")
                response = redirect("employee_home_view")
                # storing data in cookies for future purpose if i back in website and return to website then i don't need to login again
                response.set_cookie("employee_id",get_employee.employee_id)
                response.set_cookie("employee_name",f'{get_employee.first_name} {get_employee.last_name}')
                response.set_cookie("role",get_employee.role)
                response.set_cookie("password",get_employee.password)
                return response
            else:
                messages.error(request,"Employee ID or Password did not match,Try again...")
                return redirect("employee_login_view")
        except Employee.DoesNotExist:
            messages.error(request,"Employee Does Not Exists...")
            return redirect("employee_login_view")
        except Exception as e:
            messages.error(request,f"ERROR:{e}")
            return redirect("employee_login_view")

    return render(request,"employee/employee_loginpage.html")


# --------employee Dashboard view------------
@login_required
def employee_home_view(request):
    return render(request,"employee/employee_dashboardpage.html")

# --------employee Logout view------------
@login_required
def employee_logout_view(request):
    response = redirect("employee_login_view")
    response.delete_cookie("employee_id")
    response.delete_cookie("employee_name")
    response.delete_cookie("password")
    messages.success(request,"You are Logged Out !!")
    return response

# --------employee Change Password view------------
@login_required
def employee_change_password_view(request):
    get_employee = Employee.objects.get(employee_id=request.COOKIES.get("employee_id"))
    if request.method=="POST":
        old_password_ = request.POST['old_password']
        new_password_ = request.POST['new_password']
        confirm_password_ = request.POST['confirm_password']

        if get_employee.password != old_password_:
            messages.error(request,"old password is incorrect !!")
            return redirect("employee_change_password_view")
    
        elif get_employee.password == (old_password_ and new_password_):
            messages.warning(request,"New Password must be different from old password ")
            return redirect("employee_change_password_view")
            
        elif new_password_ != confirm_password_ :
            messages.error(request,"Both Passwords are not match!!")
            return redirect("employee_change_password_view")
        
        else:
            get_employee.password = new_password_
            get_employee.save()
            messages.success(request,"Your Password Updated Successfully !!")
            
            response =  redirect("employee_login_view")
            response.set_cookie("password",get_employee.password)
            return response
  
    return render(request,"employee/employee_changepassword.html",{})

@login_required
def employee_student_view(request):
    return render(request,"employee/employee_studentpage.html",{})


def employee_profile_view(request):
    return render(request,"employee/employee_profilepage.html",{})