from django.urls import path
from . import views

urlpatterns = [
    path('', views.mycospace, name='mycospace'),  # Main mycospace URL
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    # Add any other URL patterns specific to the mycospace app
]