from django.contrib import admin
from django.urls import path
from .views import EmployeeListView, UserListView
urlpatterns = [
    path("api/employee/", EmployeeListView ),
    path("api/user/", UserListView ),
]
