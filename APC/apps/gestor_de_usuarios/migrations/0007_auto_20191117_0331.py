# Generated by Django 2.2.4 on 2019-11-17 08:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_usuarios', '0006_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='nombre_responsable',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='telefono',
        ),
        migrations.AddField(
            model_name='servicio',
            name='calificacion',
            field=models.FloatField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='servicio',
            name='cantidad_calif',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo',
            field=models.CharField(choices=[('Adopción', 'Adopción'), ('Esterilización', 'Esterilización'), ('Vacunación', 'Vacunación'), ('Feria de mascotas', 'Feria de mascotas')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='direccion',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor_de_usuarios.Profile'),
        ),
    ]
