from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('calculate-pay/', views.calculate_pay, name='calculate_pay'),
]