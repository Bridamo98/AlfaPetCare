# Generated by Django 2.2.4 on 2019-11-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0015_auto_20191117_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento_global',
            name='direccion',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
