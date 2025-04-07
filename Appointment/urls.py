from django.urls import path
from . import views

urlpatterns = [
    path('list', views.appointment_list, name='appointment_list'),
    path('add/', views.add_appointment, name='add_appointment'),
]
