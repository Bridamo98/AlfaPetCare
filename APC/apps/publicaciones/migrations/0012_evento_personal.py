# Generated by Django 2.2.4 on 2019-11-17 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0018_auto_20191115_1805'),
        ('publicaciones', '0011_auto_20191116_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento_personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_evento', models.CharField(choices=[('Vacunación', 'Vacunación'), ('Desparasitación', 'Desparasitación'), ('Baño', 'Baño'), ('Consulta veterinaria', 'Consulta veterinaria')], max_length=256)),
                ('fecha_hora_evento', models.DateTimeField(default=None)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor_de_mascotas.Mascota')),
            ],
        ),
    ]
