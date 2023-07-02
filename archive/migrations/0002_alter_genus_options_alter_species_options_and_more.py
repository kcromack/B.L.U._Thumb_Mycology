# Generated by Django 4.2 on 2023-05-07 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genus',
            options={'verbose_name_plural': 'Genus'},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name_plural': 'Species'},
        ),
        migrations.AlterModelOptions(
            name='substrate',
            options={'verbose_name_plural': 'Substrate'},
        ),
        migrations.AlterModelOptions(
            name='variety',
            options={'verbose_name_plural': 'Variety'},
        ),
        migrations.RenameField(
            model_name='substrate',
            old_name='subsrtate_name',
            new_name='substrate_name',
        ),
    ]