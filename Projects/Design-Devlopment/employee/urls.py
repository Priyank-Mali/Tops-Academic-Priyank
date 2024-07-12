from django.urls import path
from . import views

urlpatterns = [
    path("",views.employee_login_view,name="employee_login_view"),
    path("dashboard/",views.employee_home_view,name="employee_home_view"),
    path("logout/",views.employee_logout_view,name="employee_logout_view"),
    path("change-password/",views.employee_change_password_view,name="employee_change_password_view"),
    path("employee-profile/",views.employee_profile_view,name="employee_profile_view"),
    path("employee-student/",views.employee_student_view,name="employee_student_view"),
    path("add-student/",views.add_student_view,name="add_student_view"),
    path("student-details/<str:student_id>/",views.student_profile_view,name="student_profile_view"),
    path("student-payment-entry/",views.student_payment_entry,name="student_payment_entry"),
    path("batch/",views.batch_view,name="batch_view"),
    path("batch-action/<str:batch_id>/",views.batch_action_view,name="batch_action_view"),

]