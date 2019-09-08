from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # we're defining Email field so that it could validate the entered Email
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    # If we want to make some changes in specific form field we can do in this way
    email = forms.EmailField(widget = forms.TextInput(attrs = {'readonly' : 'readonly'}))  # we're defining Email field so that it could validate the entered Email
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']