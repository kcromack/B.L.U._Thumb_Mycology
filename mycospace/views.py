from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from mycospace.models import UserProfile
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            
            user.save()
            # Create a user profile for a newly register user
            user_profile = UserProfile.objects.create(user=user)
            # Handle the avatar upload
            avatar = form.cleaned_data.get('avatar')
            if avatar:
                user_profile.avatar = avatar
                user_profile.save()

            # Log in the user
            login(request, user)

            messages.success(request, f'Welcome to B.L.U. Thumb Mycology. An Account was created for {user.username}.')
            return redirect('mycospace') 

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('mycospace')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the desired page after login, e.g., archive_home
            return redirect('mycospace')
    
    # If it's a GET request or authentication failed, render the arc_home.html template
    return render(request, 'archives.html')

@login_required
def mycospace(request):
    # Your view logic here
    return render(request, 'mycospace.html')

