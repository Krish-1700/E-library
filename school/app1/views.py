from lib2to3.fixes.fix_input import context

import django.contrib.auth.models

from django.contrib.auth.management.commands.changepassword import UserModel
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from app1.models import School

from app1.models import Student

from app1.forms import Registerform


class Home(TemplateView):
    template_name = "home.html"

from  app1.forms import Schoolform
class AddSchool(CreateView):
    # fields =  ['name','principal','location']
    form_class = Schoolform
    template_name = "addschool.html"
    model = School
    success_url = reverse_lazy('Home')

class AddStudent(CreateView):
    fields = ['name','age','school']
    template_name = "addstudent.html"
    model = Student
    success_url = reverse_lazy('Home')

class SchoolList(ListView):
    template_name = "schoollist.html"
    model = School
    context_object_name = "school"



class SchoolDetail(DetailView):
    model = School
    template_name = "details.html"
    context_object_name = "detail"

class StudentList(ListView):
    model = Student
    template_name = "studentlist.html"
    context_object_name = "stu"

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(school__location="Ekm")
    #     return queryset
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(name__icontains="i")
    #     return queryset
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(age="21")
    #     return queryset

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(name__startswith="s")
    #     return queryset

    def get_context_data(self):
        context=super().get_context_data()
        context['name']="Arun"
        context['school']=School.objects.all()
        return context

from django.contrib.auth.models import  User
class Register(CreateView):
    model = User
    form_class = Registerform
    # fields = ['username','password','email','first_name','last_name']
    template_name = "register.html"
    success_url =reverse_lazy("Home")

    def form_valid(self, form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']

        u=User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
        u.save()
        return redirect('Home')

class Login(LoginView):
    template_name = "login.html"


from django.contrib.auth import logout
from django.views.generic import View
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('Login')


