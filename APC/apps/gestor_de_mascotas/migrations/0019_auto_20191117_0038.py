# Generated by Django 2.2.4 on 2019-11-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_de_mascotas', '0018_auto_20191115_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, default='mascotas/anonima.jpg', null=True, upload_to='mascotas/'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(choices=[('', '---------'), ('Normal', 'Normal'), ('Perdido', 'Perdido'), ('Adopción', 'Adopcion'), ('Maltratado', 'Matratado'), ('Accidentado', 'Accidentado'), ('Encontrado', 'Encontrado')], max_length=15),
        ),
    ]