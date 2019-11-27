from rest_framework import generics
from .models import Employee, Leave
from .serializers import EmployeeSerializer, LeaveSerializer



class ListEmployeesView(generics.ListAPIView):
    queryset = Employee.employee.all()
    serializer_class = EmployeeSerializer


class PostLeaveView(generics.CreateAPIView):
    queryset = Leave.leave.all()
    serializer_class = LeaveSerializer