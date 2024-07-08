from django.urls import path
from .import views

urlpatterns = [
    path('snippets/',views.snippet_list),
    path('snippet/<int:pk>/',views.snippet_details),
]
