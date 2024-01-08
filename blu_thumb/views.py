from django.shortcuts import render

def test_base(request):
    return render(request, 'base.html')

def test_myco_base(request):
    return render(request, 'myco_base.html')