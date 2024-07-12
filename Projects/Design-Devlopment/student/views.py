from django.shortcuts import render

# Create your views here.
def student_home_view(request):
    return render(request,"student/student_homepage.html",{})