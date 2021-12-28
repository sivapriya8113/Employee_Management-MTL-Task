from django.urls import path

from . import views
from rest_framework import permissions

from .views import EmployeeList, EmployeeDetail

urlpatterns = [

    path('api/employee_list/', EmployeeList.as_view(), name='employee-list'),
    path('api/employee_detail/<str:pk>/', EmployeeDetail.as_view(), name='employee-detail'),


]