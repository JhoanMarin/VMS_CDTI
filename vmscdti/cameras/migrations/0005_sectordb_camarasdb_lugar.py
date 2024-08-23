# Generated by Django 5.0.7 on 2024-08-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0004_delete_bloquesdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='NombreSector')),
            ],
            options={
                'verbose_name': 'sector',
                'verbose_name_plural': 'sectores',
                'db_table': 'sectores',
            },
        ),
        migrations.AddField(
            model_name='camarasdb',
            name='lugar',
            field=models.CharField(default='Lugar Predeterminado', max_length=80, verbose_name='NombreUsuario'),
            preserve_default=False,
        ),
    ]
