# Generated by Django 2.2.4 on 2019-11-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0002_auto_20191105_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.CharField(choices=[('', '---------')], default=None, max_length=30),
        ),
    ]
