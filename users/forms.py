from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
    max_length=100,
    required = True,
    widget=forms.TextInput(attrs={'class': 'form-control', 
                                  'placeholder': 'Enter your E-mail',
                                  'style': 'border: none;'}),
    )
    first_name = forms.CharField(
    max_length=100,
    required = True,
    widget=forms.TextInput(attrs={'class': 'form-control', 
                                  'placeholder': 'Enter your First Name',
                                  'style': 'border: none;'}),
    )
    last_name = forms.CharField(
    max_length=100,
    required = True,
    widget=forms.TextInput(attrs={'class': 'form-control', 
                                  'placeholder': 'Enter your Last Name',
                                  'style': 'border: none;'}),
    )
    username = forms.CharField(
    max_length=25,
    required = True,
    widget=forms.TextInput(attrs={'class': 'form-control', 
                                  'placeholder': 'Enter a unique Username',
                                  'style': 'border: none;'}),
    )
    password1 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Enter a Password',
                                      'style': 'border: none;'}),
    )
    password2 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                      'placeholder': 'Enter the Password again',
                                      'style': 'border: none;'}),
    )
    CHOICES = [('yes', 'Yes'), ('no', 'No')]
    cultivator = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        required=True,
        help_text='Are you ACTIVELY cultivating?' )
    check = forms.BooleanField(required = True)

class Meta:
    model = User
    fields = [
    'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'cultivator' 'check',
    ]