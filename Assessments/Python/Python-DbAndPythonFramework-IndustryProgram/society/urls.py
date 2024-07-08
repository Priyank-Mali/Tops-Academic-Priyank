from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('dashboard/',views.dashboard_view,name='dashboard_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('members/',views.members_view,name="members_view"),
    path('watchman/',views.watchmans_view,name="watchmans_view"),
    path('notice/',views.notice_view,name="notice_view"),
    path('event/',views.event_view,name="event_view"),
    path('delete-member/<member_id>/',views.member_delete_view,name="member_delete_view"),
    path('delete-watchmen/<watchmen_id>/',views.watchman_delete_view,name="watchman_delete_view"),
    path('profile/',views.profile_view,name="profile_view"),
    path('visitor/',views.visitors_view,name="visitors_view"),
    path('change-password/',views.change_password,name="change_password"),
    path('registration/',views.registration,name="registration"),
    path('forgot-password/',views.forget_password,name="forget_password"),

]
