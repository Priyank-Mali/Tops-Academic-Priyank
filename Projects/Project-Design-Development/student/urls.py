from django.urls import path
from . import views

urlpatterns = [
    path("",views.student_home_view,name="student_home_view"),
]
