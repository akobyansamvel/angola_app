# Generated by Django 5.0.6 on 2024-05-28 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('hospital', '0004_remove_hospital_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='hospital.hospital', verbose_name='Больница'),
        ),
    ]
