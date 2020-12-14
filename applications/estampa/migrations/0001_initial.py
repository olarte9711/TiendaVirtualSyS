# Generated by Django 3.1.4 on 2020-12-14 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estampa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.TextField()),
                ('tema', models.CharField(choices=[('5', 'OTRO'), ('0', 'DEPORTE'), ('1', 'ARTE'), ('2', 'MUSICA'), ('3', 'TECNOLOGIA'), ('4', 'PELICULAS')], max_length=1, verbose_name='TEMA')),
                ('popularidad', models.CharField(choices=[('0', 'BAJA'), ('2', 'ALTA'), ('1', 'MEDIA')], max_length=1, verbose_name='Popularidad')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artista.artista')),
            ],
            options={
                'verbose_name': 'Estampa',
                'verbose_name_plural': 'Estampas',
            },
        ),
    ]
