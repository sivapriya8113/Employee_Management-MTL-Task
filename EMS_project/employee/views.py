from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import employeeserializer
from .models import Employee
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeserializer
    permission_classes = (IsAuthenticated,)


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeserializer
    permission_classes = (IsAuthenticated,)