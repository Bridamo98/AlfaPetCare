# Generated by Django 2.2.4 on 2019-11-01 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_usuarios', '0002_auto_20191030_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tfno',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
