from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg', blank=True, null=True)
    # Add other fields as needed for your user profile

    def __str__(self):
        return self.user.username
