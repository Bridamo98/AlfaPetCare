# Generated by Django 2.2.4 on 2019-11-14 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_conversacion_global_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversacion_global',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
