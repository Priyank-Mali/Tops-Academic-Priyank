from django.urls import path
from . import views

urlpatterns = [
    path('',views.customer_login_view,name='customer_login_view'),
    path('registration/',views.customer_registration_view,name='customer_registration_view'),
    path('dashboard/',views.customer_dashboard_view,name='customer_dashboard_view'),
    path('logout/',views.customer_logout_view,name='customer_logout_view'),
]
