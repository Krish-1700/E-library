"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.core.management.commands.runserver import naiveip_re
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="Home"),
    path('AddSchool',views.AddSchool.as_view(),name="AddSchool"),
    path('AddStudent',views.AddStudent.as_view(),name="AddStudent"),
    path('SchoolList',views.SchoolList.as_view(),name="SchoolList"),
    path('SchoolDetail/<int:pk>',views.SchoolDetail.as_view(),name="SchoolDetail"),
    path('StudentList',views.StudentList.as_view(),name="StudentList"),
    path('Register',views.Register.as_view(),name="Register"),
    path('Login',views.Login.as_view(),name="Login"),
    path('Logout',views.Logout.as_view(),name="Logout"),
]
