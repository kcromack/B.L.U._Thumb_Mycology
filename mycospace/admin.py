from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')  # Add other fields as needed

admin.site.register(UserProfile, UserProfileAdmin)
