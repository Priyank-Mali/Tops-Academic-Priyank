from django.shortcuts import render,redirect
from django.contrib import messages
from functools import wraps
from django.urls import reverse

from .models import Employee

from student.models import Student,StudentProfile,StudentAddress,StudentCourse,StudentPayment,StudentPaymentEntry
from student.forms import StudentForm

from employee.models import Batch,AssignBatch
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
    batches = Batch.objects.all()
    students = AssignBatch.objects.all()
    batch_data = []
    if request.COOKIES.get('role') == 'counsellor':
        for batch in batches:
            total_student = 0
            for student in students:
                if (student.batch_id.faculty_id_id == batch.faculty_id_id ) and (batch.technology_id == student.batch_id.technology_id ):
                    total_student += 1
            batch_data.append({'batch' : batch , 'total_student' : total_student })
        
    context = {
        'batches' : batch_data,
    }
    return render(request,"employee/employee_dashboardpage.html",context)


# --------employee Logout view------------
@login_required
def employee_logout_view(request):
    response = redirect("employee_login_view")
    response.delete_cookie("employee_id")
    response.delete_cookie("employee_name")
    response.delete_cookie("password")
    messages.success(request,"You are Logged Out !!")
    return response


# -------- employee Change Password view ------------
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


# ------------- employee profile details/change using model view -----------------------
@login_required
def employee_profile_view(request):
    employee_object = Employee.objects.get(employee_id = request.COOKIES.get('employee_id'))
    print(employee_object)
    if request.method == 'POST':
        first_name_ = request.POST.get('first_name')
        last_name_ = request.POST.get('last_name')
        mobile_ = request.POST.get('mobile')

        employee_object.first_name = first_name_
        employee_object.last_name = last_name_
        employee_object.mobile = mobile_

        employee_object.save()
        response = redirect("employee_profile_view")
        response.set_cookie('employee_name',f'{employee_object.first_name} {employee_object.last_name}')
        messages.success(request,"Profile Changes Successfully")
        return response

    context = {
        'employee' : employee_object
    }
    return render(request,"employee/employee_profilepage.html",context)


# ---------- employee / student list view ----------------------
@login_required
def employee_student_view(request):
    students_objects = Student.objects.all().order_by("-created_at")

    context = {
        'students' : students_objects,
        'student_form' : StudentForm()

    }
    return render(request,"employee/employee_studentpage.html",context)


# ------------------- add student view ------------------------
@login_required
def add_student_view(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        print(student_form)
        if student_form.is_valid():
            student_form.save()
            messages.success(request,'student add successfully')
            return redirect("employee_student_view")
        else:
            messages.error(request,'Invalid Form')
            return redirect("employee_student_view")
    return redirect("add_student_view")


# ----------------- student profile view ----------------------------------
@login_required
def student_profile_view(request,student_id):
    context = {}

    try:
        get_student = Student.objects.get(student_id=student_id)
        context['student'] = get_student
    except Student.DoesNotExist:
        context['student'] = {
            'status_code': 404,
            'message': "Student data not found"
        }
    
    try:
        get_student_profile = StudentProfile.objects.get(student_id_id=student_id)
        context['student_profile'] = get_student_profile
    except StudentProfile.DoesNotExist:
        context['student_profile'] = {
            'status_code': 404,
            'message': "Student profile data not found"
        }

    try:
        get_student_address = StudentAddress.objects.get(student_id_id=student_id)
        context['student_address'] = get_student_address
    except StudentAddress.DoesNotExist:
        context['student_address'] = {
            'status_code': 404,
            'message': "Student address not found"
        }

    try:
        get_student_course = StudentCourse.objects.get(student_id_id=student_id)
        context['student_course'] = get_student_course
    except StudentCourse.DoesNotExist:
        context['student_course'] = {
            'status_code': 404,
            'message': "Student course not found"
        }

    try:
        get_student_account = StudentPayment.objects.get(student_id_id=student_id)
        context['student_account'] = get_student_account
    except StudentPayment.DoesNotExist:
        context['student_account'] = {
            'status_code': 404,
            'message': "Student payment account not found"
        }
    
    try:
        get_student_payment_entries = StudentPaymentEntry.objects.filter(student_id_id=student_id)
        context['student_payment_entries'] = get_student_payment_entries
    except StudentPaymentEntry.DoesNotExist:
        context['student_payment_entries'] = {
            'status_code': 404,
            'message': "Student payment entry not found"
        }

    return render(request,'employee/employee_studentdetailview.html',context)


@login_required
def student_payment_entry(request):
    if request.method == "POST":
        student_id_ = request.POST.get("student_id")
        proof_ = request.FILES.get("proof")
        paid_date_ = request.POST.get("paid_date")
        installment_ = request.POST.get("installment")

        print(student_id_,proof_,paid_date_,installment_)
        new_payment = StudentPaymentEntry(
            student_id_id = student_id_,
            proof = proof_,
            paid_date = paid_date_,
            installment = installment_
        )
        new_payment.save()
        print(new_payment)
        messages.success(request,f"{installment_} is successfully paid for {student_id_}")
        return redirect(reverse('student_payment_entry'),args=[student_id_])
        # return redirect("student_payment_entry")


@login_required
def batch_view(request):
    students = AssignBatch.objects.all()
    if request.COOKIES.get('role') == 'counsellor':
        batches = Batch.objects.all()

    elif request.COOKIES.get('role') == 'faculty':
        employee_object = Employee.objects.get(employee_id = request.COOKIES.get('employee_id'))
        batches = Batch.objects.filter(faculty_id_id = employee_object.employee_id)
    
    context = {
        'batches' : batches, 
        'students' : students
    }
   
    return render(request,"employee\employee_batch_view.html",context)


def batch_action_view(request,batch_id):
    batch_object = Batch.objects.get(batch_id = batch_id)
    get_students = AssignBatch.objects.filter(batch_id_id = batch_id)
    
    context = {
        'batch' : batch_object,
        'students' : get_students
    }
    return render(request,'employee/employee_batch_action_view.html',context)

