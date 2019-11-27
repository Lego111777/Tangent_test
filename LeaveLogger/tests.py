from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Employee, Leave
from .serializers import EmployeeSerializer, LeaveSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_employee(emp_number="", phone_number="", first_name="", last_name=""):
        if emp_number != "" and phone_number != "" and first_name != "" and last_name != "":
            Employee.employee.create(emp_number=emp_number, phone_number=phone_number, first_name=first_name , last_name=last_name )

    def setUp(self):
        # add test data
        self.create_employee("emp001t", "0113116412", "TestName001", "TestSurname001")
        self.create_employee("emp002t", "0113116413", "TestName002", "TestSurname002")
        self.create_employee("emp003t", "0113116414", "TestName003", "TestSurname003")
        self.create_employee("emp004t", "0113116415", "TestName004", "TestSurname004")


class GetAllEmployeesTest(BaseViewTest):

    def test_get_all_employees(self):
        """
        This test ensures that all employees added in the setUp method
        exist when we make a GET request to the employees/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("employees-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Employee.employee.all()
        serialized = EmployeeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)