# Generated by Django 2.2.4 on 2019-11-17 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0022_evento_personal_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento_personal',
            name='usuario',
        ),
    ]