# Generated by Django 2.2.4 on 2019-11-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0014_auto_20191117_0021'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lugar',
        ),
        migrations.AlterField(
            model_name='evento_global',
            name='fecha_hora_evento_final',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='evento_global',
            name='fecha_hora_evento_inicio',
            field=models.DateTimeField(),
        ),
    ]
