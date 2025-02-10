from django import forms
from django.contrib.auth.backends import UserModel
from django.forms import PasswordInput


class Registerform(forms.ModelForm):
    password=forms.CharField(widget=PasswordInput)
    confirm_password=forms.CharField(widget=PasswordInput)

    class Meta:
        model=UserModel
        fields=['username','password','confirm_password','email','first_name','last_name']


