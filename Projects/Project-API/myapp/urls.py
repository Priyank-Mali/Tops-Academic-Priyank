from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentList,name="studentList"),
    path('student/<str:student_id>/',views.studentDetails,name="studentDetails"),
]
