from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('new', 'New'),
    ('app', 'Approved'),
    ('decl', 'Declined'),
)


class Employee(models.Model):
    employee = models.Manager()
    emp_number = models.CharField(max_length=10, primary_key=True)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.emp_number)

class Leave(models.Model):
    leave = models.Manager()
    employee_pk = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    days_of_leave = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return "{} ({}) to ({})".format(self.employee_pk, self.start_date, self.end_date)
