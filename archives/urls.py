from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import search

urlpatterns = [
    path('', views.archives, name='archives'), # Default route is set to archives 
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)