# Generated by Django 4.2 on 2023-11-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycospace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_avatar.jpg', null=True, upload_to='avatars/'),
        ),
    ]