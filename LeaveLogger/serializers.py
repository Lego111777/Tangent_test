from rest_framework import serializers
from .models import Employee, Leave
from datetime import datetime

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_number', 'phone_number', 'first_name', 'last_name']


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['employee_pk', 'start_date', 'end_date', 'days_of_leave', 'status']

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        leave_days = data['end_date'] - data['start_date']
        leave_days = str(leave_days)
        leave_days.split(" ")
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")
        if  leave_days[0] != data['days_of_leave']:
            raise serializers.ValidationError("date difference does not amount to days of leave requested {}".format(leave_days))
        return data