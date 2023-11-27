from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

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
    
    avatar = forms.ImageField(
        required=False,  # Set this to True if you want the avatar to be mandatory
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        help_text='Upload your avatar'
    )

    CHOICES = [('yes', 'Yes'), ('no', 'No')]
    cultivator = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        required=True,
        help_text='Are you ACTIVELY cultivating?' )
    check = forms.BooleanField(required = True)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()

            # Create a user profile for the newly registered user
            user_profile = UserProfile.objects.create(user=user)
            # Handle the avatar upload
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                user_profile.avatar = avatar
                user_profile.save()

        return user

class Meta:
    model = User
    fields = [
    'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'cultivator' 'check',
    ]