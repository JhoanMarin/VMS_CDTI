# Generated by Django 5.0.7 on 2024-08-22 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0005_sectordb_camarasdb_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='camarasdb',
            name='sector_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cameras.sectordb'),
            preserve_default=False,
        ),
    ]
