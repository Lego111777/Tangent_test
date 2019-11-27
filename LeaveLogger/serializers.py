from rest_framework import serializers
from .models import Employee, Leave

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_number', 'phone_number', 'first_name', 'last_name']


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['employee_pk', 'start_date', 'end_date', 'days_of_leave', 'status']