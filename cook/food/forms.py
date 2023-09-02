# Import all necessary functions
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Define a class that will create a form that will allow the user to register as a new user.
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email_address = forms.CharField()
    

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email_address', 'password1', 'password2']