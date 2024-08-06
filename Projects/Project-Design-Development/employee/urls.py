from django.urls import path
from . import views

urlpatterns = [
    path("",views.employee_login_view,name="employee_login_view"),
    path("dashboard/",views.employee_home_view,name="employee_home_view"),
    path("logout/",views.employee_logout_view,name="employee_logout_view"),
    path("change-password/",views.employee_change_password_view,name="employee_change_password_view"),
    path("employee-student/",views.employee_student_view,name="employee_student_view"),
    path("employee-profile/",views.employee_profile_view,name="employee_profile_view"),
    path("student-details/<str:student_id>/",views.student_details_view,name="student_details_view"),
    path("add-student/",views.add_student_view,name="add_student_view"),
    path("batch/",views.batch_view,name="batch_view"),
    path("batch-action/<str:batch_id>/",views.batch_action_view,name="batch_action_view"),
    path("mybatch/",views.mybatch_view,name="mybatch_view"),
    path("student-payment-entry/",views.student_payment_entry_view,name="student_payment_entry_view"),
    path("add-global-note/",views.add_global_note,name="add_global_note"),
    path("update-global-note/",views.update_global_note,name="update_global_note"),
    path("delete-global-note/<int:note_id>/",views.delete_global_note,name="delete_global_note"),

]
