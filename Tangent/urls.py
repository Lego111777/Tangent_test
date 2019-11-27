from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path(r'swagger-docs/', schema_view),
    path('admin/', admin.site.urls),
    re_path('api/', include('LeaveLogger.urls')),
]
