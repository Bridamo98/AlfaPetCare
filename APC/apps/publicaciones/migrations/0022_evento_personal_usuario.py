# Generated by Django 2.2.4 on 2019-11-17 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_usuarios', '0008_auto_20191117_1113'),
        ('publicaciones', '0021_auto_20191117_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento_personal',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestor_de_usuarios.Profile'),
        ),
    ]