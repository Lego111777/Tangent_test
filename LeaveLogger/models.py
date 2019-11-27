from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('new', 'New'),
    ('app', 'Approved'),
    ('decl', 'Declined'),
)


class Employee(models.Model):
    emp_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Leave(models.Model):
    employee_pk = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    days_of_leave = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')