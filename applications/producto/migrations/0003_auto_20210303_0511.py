# Generated by Django 3.0.6 on 2021-03-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20210303_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estampa',
            name='popularidad',
            field=models.CharField(choices=[('0', 'BAJA'), ('2', 'ALTA'), ('1', 'MEDIA')], max_length=1, verbose_name='Popularidad'),
        ),
        migrations.AlterField(
            model_name='estampa',
            name='tema',
            field=models.CharField(choices=[('3', 'TECNOLOGIA'), ('4', 'PELICULAS'), ('5', 'OTRO'), ('1', 'ARTE'), ('0', 'DEPORTE'), ('2', 'MUSICA')], max_length=1, verbose_name='TEMA'),
        ),
    ]
