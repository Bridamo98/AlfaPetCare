# Generated by Django 2.2.4 on 2019-11-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0019_evento_global_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento_global',
            name='latitud',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='evento_global',
            name='longitud',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
