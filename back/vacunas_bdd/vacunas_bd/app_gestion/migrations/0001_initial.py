# Generated by Django 4.0.5 on 2022-06-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_vacuna',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre')),
                ('apellido_materno', models.CharField(max_length=15, verbose_name='Apellido Materno')),
                ('apellido_paterno', models.CharField(max_length=15, verbose_name='Apellido Materno')),
                ('edad', models.IntegerField()),
                ('vacuna', models.CharField(max_length=20, verbose_name='Nombre Vacuna')),
                ('tip_vacuna', models.CharField(max_length=20, verbose_name='Tipo Vacuna')),
                ('fecha', models.DateField()),
            ],
        ),
    ]