from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepages'),
    path('doctor/list', views.doctor_list, name='doctor_list'),
    path('doctor/add/', views.add_doctor, name='add_doctor'),
]