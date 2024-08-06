from django.shortcuts import render,redirect
from functools import wraps
from .models import Employee,Batch,AssignBatch
from django.contrib import messages
from django.urls import reverse

from master.models import Technology

from student.models import Student,StudentProfile,studentAddress,StudentCourse,StudentPayment,StudentPaymentEntry
from student.forms import StudentForm

from .forms import StudentPaymentForm

from decimal import Decimal

import requests
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

# -------------------------- Decorater for authorization --------------------------
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

# ----------------------- employee login view --------------------------
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


# ------------------------employee Dashboard view ---------------------
@login_required
def employee_home_view(request):
    batch_data = []
    if request.COOKIES['role'] == 'counsellor':
        batches = Batch.objects.all()
        students = AssignBatch.objects.all()

        for batch in batches:
            total_student = 0
            for student in students:
                if (student.batch_id.faculty_id_id == batch.faculty_id_id )and (batch.technology_id == student.batch_id.technology_id ):
                    total_student += 1
                    logo = student.batch_id.technology_id.logo
            batch_data.append({'batch' : batch , 'total_student' : total_student ,'logo' : logo })
    
    elif request.COOKIES['role'] == 'faculty':
        batch = Batch.objects.get(faculty_id_id = request.COOKIES.get('employee_id'))
        students = AssignBatch.objects.filter(batch_id_id = batch.batch_id).count()

    context = {
        'batches' : batch_data,
        'students' : students,
        'mybatch' : batch

    }
    return render(request,"employee/employee_dashboardpage.html",context)

# ---------------------------- employee Logout view ---------------------
@login_required
def employee_logout_view(request):
    response = redirect("employee_login_view")
    response.delete_cookie("employee_id")
    response.delete_cookie("employee_name")
    response.delete_cookie("password")
    messages.success(request,"You are Logged Out !!")
    return response

# ----------------------- employee Change Password view ---------------------
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

# ---------- employee / student list view ----------------------
@login_required
def employee_student_view(request):
    students_objects = Student.objects.all().order_by("-created_at")

    context = {
        'students' : students_objects,
        'student_form' : StudentForm()

    }
    return render(request,"employee/employee_studentpage.html",context)

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

# ----------------- student profile view ----------------------------------
@login_required
def student_details_view(request,student_id):
    
    context = {}

    try:
        student_object = Student.objects.get(student_id = student_id)
        context["student"] = student_object
    except Student.DoesNotExist:
        context['student'] = {
            "status_code" : 404,
            "message" : "student data not found"
        }
    try:
        student_profile = StudentProfile.objects.get(student_id_id = student_id)
        context["student_profile"] = student_profile
    except StudentProfile.DoesNotExist:
        context["student_profile"] = {
            "status_code" : 404,
            "message" : "student Profile not found"
        }
    try:
        student_address = studentAddress.objects.get(student_id_id = student_id)
        context["student_address"] = student_address
    except studentAddress.DoesNotExist:
        context['student_address'] = {
            "status_code" : 404,
            "message" : "Student Address Not Found"
        }

    try:
        student_course = StudentCourse.objects.get(student_id_id = student_id)
        context['student_course'] = student_course
    except StudentCourse.DoesNotExist:
        context["student_course"] = {
            "status_code" : 404,
            "message" : "Student Course Not Found"
        }
    try:
        student_payment = StudentPayment.objects.get(student_id_id = student_id)
        context['student_payment']  = student_payment
    except StudentPayment.DoesNotExist:
        context["student_payment"] = {
            "status_code" : 404,
            "message" : "Student Payment Entry Not Found"
        }
    
    try:
        student_payment_entry = StudentPaymentEntry.objects.filter(student_id_id = student_id)
        context['student_payment_entry'] = student_payment_entry
    except StudentPaymentEntry.DoesNotExist:
        context['student_payment_entry'] = {
            "status_code" : 404
        }
    
    # form = StudentPaymentForm()
    # context['paymentform'] = form

    # context = {
    #     'student' : student_object,
    #     'student_profile' : student_profile,
    #     # 'student_address' : student_address,
    # }
    return render(request,'employee/employee_studentdetailview.html',context)

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
        
# -------------------- batch View ----------------------------------
@login_required
def batch_view(request):
    if request.COOKIES.get('role') == 'counsellor':
        batches = Batch.objects.all()
    elif request.COOKIES.get('role') == '':
        get_employee = Employee.objects.get(faculty_id = request.COOKIES.get("employee_id"))
        batches = Batch.objects.filter(faculty_id_id = get_employee.employee_id)
    get_student = AssignBatch.objects.all()
    context = {
        'batches' : batches,
        'students' : get_student
    }
    return render(request,"employee/employee_batch_view.html",context)

# -------------------- employee specific Batch View -----------------------------
@login_required
def mybatch_view(request):
    batch = Batch.objects.get(faculty_id_id = request.COOKIES.get('employee_id'))
    students = AssignBatch.objects.filter(batch_id_id = batch.batch_id)
   
    batch_student_note = []
    for student in students:
        url = f"http://127.0.0.1:2000/student/{student.student_id_id}/"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            for single_data in json_data["payload"]:
                batch_student_note.append(single_data)
    print(batch_student_note)
    # sorted_notes_data = sorted(batch_student_note, key=lambda x: x['created_at'])
    # print(sorted_notes_data)
    context = {
        'batch' : batch,
        'students' : students,
    }

    return render(request,'employee/employee_mybatch.html',context)

# --------------------- Batch Action View ------------------------------------------
@login_required
def batch_action_view(request,batch_id):
    return render(request,"employee/employee_student_batch_action.html")

# ----------------------- student payment entry -----------------------------
@login_required
def student_payment_entry_view(request):
    if request.method=='POST':
        student_id_ = request.POST.get('student_id')
        proof_ = request.FILES.get('proof')
        paid_date_ = request.POST.get('paid_date')
        installment_ = request.POST.get('installment')

        student_payment_object = StudentPayment.objects.get(student_id_id=student_id_)
        if Decimal(installment_) > student_payment_object.remaining_fees:
            messages.error(request,"payment should be less or equal to remaining fees")
        
        StudentPaymentEntry.objects.create(
            student_id_id = student_id_,
            proof = proof_,
            paid_date = paid_date_,
            installment = Decimal(installment_)
        )
        messages.success(request,f"{installment_} Rs. Payment Added to {student_id_} Account")
        return redirect(reverse("student_details_view" ,args=[student_id_]))
    

# -------------------------------- add global note ----------------------------
def add_global_note(request):
    if request.method == "POST":
        student_id_ = request.POST.get("student_id")
        comment_ = request.POST.get("comment")

        jsondata = {
            "student_id" : student_id_,
            "comment" : comment_
        }
        url = "http://127.0.0.1:2000/students/"
        response = requests.post(url,data=jsondata)
        print(response)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            if response_data.get("status_code")==201:
                messages.success(request,"global note added successfully.")
            else:
                print(response_data.get("error"))
                messages.error(request,str(response_data.get("error")))
        else:
            messages.error(request,"something went wrong")
 
    return redirect("mybatch_view")
    

    