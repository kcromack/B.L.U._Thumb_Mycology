from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    
    if request.method == 'POST':
        form  = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, f'Welcome to B.L.U. Thumb Mycology. An Account was created for {user}.' )
        return redirect('archive_home')
    
    else: 
        print('Form is not valid')
    
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'register.html', context)
     
