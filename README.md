This is a Django rest API created for test by Tangent solutions.

To run this project follow the steps.

1   run pip install -r requirements
2   run python manage,py makemigrations LeaveLogger
3   run python manage.py migrate
4   run python manage.py createsuperuser
5   run python manage.py runserver

After completing the above steps the rest frameworks should be hosted on your local machine IE (http://127.0.0.1:8000/)
Once you have hosted the server please go to the admin panel IE (http://127.0.0.1:8000/admin) and add an employee.
To request leave use the (emp_number) as the employee_pk.

To see the documentaion please go to this url (http://127.0.0.1:8000/swagger-docs/) that should be the default unless changed.
