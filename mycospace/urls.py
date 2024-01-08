from django.urls import path
from . import views

urlpatterns = [
    path('', views.mycospace, name='mycospace'),  # Main mycospace URL
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # Add any other URL patterns specific to the mycospace app
]