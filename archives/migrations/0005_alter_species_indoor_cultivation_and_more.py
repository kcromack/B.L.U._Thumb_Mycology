# Generated by Django 4.2 on 2023-06-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_alter_genus_options_genus_fav_eco_genus_geo_loc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='indoor_cultivation',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='species',
            name='medicinal',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
