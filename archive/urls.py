from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import search

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/<str:genus>/', views.index, name='index'),
    path('search/', search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)