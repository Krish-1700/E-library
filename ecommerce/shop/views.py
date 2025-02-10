from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from shop.models import Category,Products

from shop.forms import Registerform
from django.contrib.auth.models import User

from cart.models import Order_details


class Home(ListView):
    model=Category
    template_name="categories.html"
    context_object_name="cat"


class Productview(DetailView):
    model=Category
    template_name="product.html"
    context_object_name="cat"

class Detail(DetailView):
    model = Products
    template_name = "details.html"
    context_object_name = "detail"

class Register(CreateView):
    model = User
    template_name = "register.html"
    form_class = Registerform
    success_url = reverse_lazy('shop:Login')

    def form_valid(self, form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']

        u=User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
        u.save()
        return redirect('shop:Login')

class Login(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy('shop:home')

from django.contrib.auth import logout
from django.views.generic import View

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('shop:Login')


class Addcategory(CreateView):
    fields = ['name','image','desc']
    template_name = "addcategory.html"
    model = Category
    success_url = reverse_lazy('shop:home')

class Addproduct(CreateView):
    fields = ['name','image','desc','price','stock','category']
    template_name = "addproducts.html"
    model = Products
    success_url = reverse_lazy('shop:home')

class Addstock(UpdateView):
    fields = ['stock']
    template_name = "addstock.html"
    model = Products
    success_url = reverse_lazy("shop:home")









