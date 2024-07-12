from django.shortcuts import render,redirect
from django.contrib import messages
from functools import wraps

from .models import Chairmans,Members,Watchmans,Notice,Event,Visitors,Role
from .forms import MembersForm,WatchmenForm,ChairmanForm,VisitorsForm


from django.core.mail import send_mail

import os
# Create your views here.

def login_required(function):
    @wraps(function)
    def wrapped_func(request,*args,**kwargs):
        if (request.COOKIES.get('chairman_id') and request.COOKIES.get('role')) or (request.COOKIES.get('role') and request.COOKIES.get('member_id')) or (request.COOKIES.get('role') and request.COOKIES.get('watchman_id')):
            return function(request,*args,**kwargs)
        else:
            messages.warning(request,'Cookies are Expire !!')
            return redirect('login_view')
    return wrapped_func


def login_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        password_ = request.POST.get('password')
        try:
            chairman_object = Chairmans.objects.filter(email = email_).first()
            if chairman_object:
                if chairman_object.password == password_:
                    response = redirect('dashboard_view')
                    response.set_cookie('chairman_id',chairman_object.chairman_id)
                    response.set_cookie('role',chairman_object.role)
                    response.set_cookie('name',f'{chairman_object.first_name} {chairman_object.last_name}')
                    messages.success(request,'Loging Successfully')
                    return response
                else:
                    messages.error(request,'email or password does\'t\' match')

            member_object = Members.objects.filter(email = email_).first()
            if member_object:
                if member_object.password == password_:
                    response = redirect('dashboard_view')
                    response.set_cookie('name',f'{member_object.first_name} {member_object.last_name}')
                    response.set_cookie('role',member_object.role)
                    response.set_cookie('member_id',member_object.member_id)
                    return response
                else:
                    messages.error(request,'email or password does\'t\' match')
            
            watchman_object = Watchmans.objects.filter(email=email_).first()
            if watchman_object:
                if watchman_object.password == password_:
                    response = redirect('dashboard_view')
                    response.set_cookie('name',f'{watchman_object.first_name} {watchman_object.last_name}')
                    response.set_cookie('role',watchman_object.role)
                    response.set_cookie('watchman_id',watchman_object.watchman_id)
                    return response
                else:
                    messages.error(request,'email or password does\'t\' match')

            messages.error(request,'Email not found')

        except Exception as e:
            messages.error(request,e)
    
    return render(request,'society/login.html')


@login_required
def dashboard_view(request):
    members = Members.objects.count()
    watchmens = Watchmans.objects.count()
    notices = Notice.objects.count()
    events = Event.objects.count()
    visitors = Visitors.objects.count()

    context = {
        'members' : members,
        'watchmens' : watchmens,
        'notices' : notices,
        'events' : events,
        'visitors' : visitors
    }
    return render(request,'society/dashboard.html',context)

@login_required
def profile_view(request):
    if request.COOKIES.get('role') == 'chairman':
        data = Chairmans.objects.get(chairman_id = request.COOKIES.get('chairman_id'))
        form = ChairmanForm(instance=data)
        if request.method=='POST':
            form = ChairmanForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                messages.success(request,'Update Successfully')
                return redirect('profile_view')
            else:
                form = ChairmanForm()

    elif request.COOKIES.get('role') == 'member':
        data = Members.objects.get(member_id = request.COOKIES.get('member_id'))
        form = MembersForm(instance=data)
        if request.method=='POST':
            form = MembersForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                messages.success(request,'Update Successfully')
                return redirect('profile_view')
            else:
                form = MembersForm()

    elif request.COOKIES.get('role') == 'watchman':
        data = Watchmans.objects.get(watchman_id=request.COOKIES.get('watchman_id'))
        form = WatchmenForm(instance=data)
        if request.method=='POST':
            form = WatchmenForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                messages.success(request,'Update Successfully')
                return redirect('profile_view')
            else:
                form = WatchmenForm()
        
    context = {
        'form' : form,
        'data' : data
    }
    return render(request,'society/profile.html',context)

@login_required
def logout_view(request):
    response = redirect('login_view')
    response.delete_cookie('role')
    response.delete_cookie('name')
    response.delete_cookie('member_id')
    response.delete_cookie('chairman_id')
    messages.success(request,'You are Logged Out !!')
    print(response)
    return response

@login_required
def members_view(request):
    members_objects = Members.objects.all()
    member_form = MembersForm(request.POST)
    if request.GET.get('search'):
        members_objects = Members.objects.filter(member_id__icontains = request.GET.get('search')
        ) | Members.objects.filter(first_name__icontains = request.GET.get('search')
        ) | Members.objects.filter(last_name__icontains = request.GET.get('search'))

    if member_form.is_valid():
        member_form.save()
        messages.success(request,'Member added Successfully')
        return redirect('members_view')
    
    member_form = MembersForm()
    
    context = {
        'members' : members_objects,
        'member_form' : member_form
    }
    return render(request,"society/society_members.html",context)


@login_required
def watchmans_view(request):
    watchmans_objects = Watchmans.objects.all()
    watchmen_form = WatchmenForm(request.POST)
    if watchmen_form.is_valid():
        watchmen_form.save()
        messages.success(request,'Added Successfully')
        return redirect('watchmans_view')
    
    watchmen_form = WatchmenForm()
    context = {
        'watchmans' : watchmans_objects,
        'watchmen_form' : watchmen_form
    }
    return render(request,"society/society_watchmans.html",context)


@login_required
def notice_view(request):
    notices_objects = Notice.objects.all()
    context = {
        'notices' : notices_objects
    }
    return render(request,"society/society_notices.html",context)

@login_required
def event_view(request):
    events_objects = Event.objects.all()
    context = {
        'events' : events_objects
    }
    return render(request,"society/society_events.html",context)

@login_required
def member_delete_view(request,member_id):
    if request.method=='POST':
        try:
            member_queryset = Members.objects.get(member_id = member_id)
            member_queryset.delete()
            messages.success(request,f'Member delete successfully.')
            return redirect('members_view')
        except member_queryset.DoesNotExist:
            messages.error(request,'This member not exists')
        except Exception as e:
            messages.error(request,e)
    messages.error(request,'Somthing Went Wrong!!')

@login_required
def watchman_delete_view(request,watchmen_id):
    if request.method=='POST':
        try:
            watchmen_queryset = Watchmans.objects.get(watchman_id = watchmen_id)
            watchmen_queryset.delete()
            messages.success(request,f'Watchmen delete successfully.')
            return redirect('watchmans_view')
        except watchmen_queryset.DoesNotExist:
            messages.error(request,'This watchmen not exists')
        except Exception as e:
            messages.error(request,e)
    messages.error(request,'Somthing Went Wrong!!')

@login_required
def visitors_view(request):
    form = VisitorsForm()
    if request.method=='POST':
        form = VisitorsForm(request.POST)
        # exit_time_ = request.POST.get('exit_time')
        if form.is_valid():
            form.save()
            messages.success(request,'Entry added')
        # elif exit_time_:
        #     pass

        messages.error(request,'Somthing Went Wrong')

    
    visitors = Visitors.objects.all()
    context = {
        'visitors' : visitors,
        'form' : form
    }
    return render(request,'society/society_visitors.html',context)


@login_required
def change_password(request):
    if request.method=="POST":
        old_password_ = request.POST.get('o_password')
        new_password_ = request.POST.get('n_password')
        c_password_ = request.POST.get('c_password')
        
        get_user = Chairmans.objects.get(chairman_id = request.COOKIES.get('chairman_id'))
        if get_user.password == old_password_:
            if new_password_ == old_password_:
                messages.error(request,'new password must be different from old password')
            elif new_password_ != c_password_:
                messages.error(request,'new password and confirm password not match')
            else:
                get_user.password = new_password_
                get_user.save()
                messages.success(request,'password change successfully')
                return redirect('login_view')

    return render(request,'society/change_password.html')


def registration(request):
    if request.method=='POST':
        role_ = request.POST.get('role')
        first_name_ = request.POST.get('first_name')
        last_name_ = request.POST.get('last_name')
        contact_ = request.POST.get('contact')
        email_ = request.POST.get('email')
        try:
            role_instance_chairman = Role.objects.get(role = 'chairman')
            role_instance_member = Role.objects.get(role = 'member')
            print(role_,role_instance_chairman)
            if role_ == "chairman":
                get_object = Chairmans.objects.filter(email = email_)
                if get_object:
                    messages.error(request,"This chairman is already exists")
                else:
                    Chairmans.objects.create(
                        role = role_instance_chairman,
                        first_name = first_name_,
                        last_name = last_name_,
                        mobile = contact_,
                        email = email_
                    )
                    messages.success(request,"registration successfull")
                    return redirect('login_view')
            elif role_ == "member":
                get_object = Members.objects.filter(email = email_)
                if get_object:
                    messages.error(request,'This member is already exists')
                else:
                    Members.objects.create(
                        role = role_instance_member,
                        first_name = first_name_,
                        last_name = last_name_,
                        mobile = contact_,
                        email = email_
                    )
                    messages.success(request,"registration successfull")
                    return redirect('login_view')
        except Role.DoesNotExist:
            messages.error(request, "Role does not exist.")
        except Exception as e:
            messages.error(request,e)
    return render(request,'society/registration.html')


def forget_password(request):
    if request.method=='POST':
        email_ = request.POST.get('email')
        try:
            get_chairman = Chairmans.objects.get(email=email_)
            if get_chairman:
                subject = 'Forgot Password'
                message = f"""Hello, {get_chairman.first_name} {get_chairman.last_name}
                You Your Login crediatila is:
                EMAIL : {get_chairman.email},
                PASSWORD : {get_chairman.password}
                """
                from_email = 'priyankmali297@gmail.com'
                recipient_list =  [get_chairman.email]

                send_mail(subject,message,from_email,recipient_list)

                messages.success(request,'Check Your Email')
                return redirect('login_view')
        except Chairmans.DoesNotExist:
            messages.error(request,'This email is not exists')
        except Exception as e:
            messages.error(request,e)
    return render(request,'society/forgot_password.html')


def watchman_update_view(request,watchman_id):
    watchman_object = Watchmans.objects.get(watchman_id=watchman_id)
    if request.method=='POST':
        first_name_ = request.POST.get('first_name')
        last_name_ = request.POST.get('last_name')
        email_ = request.POST.get('email')
        mobile_ = request.POST.get('mobile')

        if first_name_:
            watchman_object.first_name = first_name_
        
        if last_name_:
            watchman_object.last_name = last_name_
        
        if email_:
            watchman_object.email = email_

        if mobile_:
            watchman_object.mobile = mobile_

        watchman_object.save()
        messages.success(request,'update successfully')
        return redirect('watchmans_view')

    else:
        messages.error(request,'somthig went wrong')
