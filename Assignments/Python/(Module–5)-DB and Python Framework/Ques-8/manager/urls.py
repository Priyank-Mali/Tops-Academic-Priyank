from django.urls import path
from . import views

urlpatterns = [
    path("",views.manager_login_view,name="manager_login_view"),
    path("dashboard/",views.manager_dashboard_view,name="manager_dashboard_view"),
    path("logout/",views.manager_logout_view,name="manager_logout_view"),
    path("edit-product/<id>",views.manager_product_edit,name="manager_product_edit"),
    path("delete-product/<int:id>/",views.manager_product_delete,name="manager_product_delete")
]
