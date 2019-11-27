from django.urls import path
from .views import ListEmployeesView, PostLeaveView


urlpatterns = [
    path('employees/', ListEmployeesView.as_view(), name="employees-all"),
    path('leave/', PostLeaveView.as_view(), name="create-leave"),
]
