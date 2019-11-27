from django.conf.urls import url
from rest_framework import generics

from .models import Employee, Leave
from .serializers import EmployeeSerializer, LeaveSerializer


class ListEmployeesView(generics.ListAPIView):
    '''
    Basic view to list all employees
    '''
    queryset = Employee.employee.all()
    serializer_class = EmployeeSerializer


class PostLeaveView(generics.CreateAPIView):
    '''
    View used to post to the Leave model and create a new object
    '''
    queryset = Leave.leave.all()
    serializer_class = LeaveSerializer
