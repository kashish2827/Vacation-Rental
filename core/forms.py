from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserSignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','role','password1','password2']
        Widget = {
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput() 
        } 

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())