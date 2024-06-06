# Generated by Django 5.0.6 on 2024-06-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passportApplication', '0005_alter_pasapp_passport_scan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasapp',
            name='passport_scan',
            field=models.ImageField(default='1', upload_to='passport_scans/', verbose_name='Скан паспорта'),
        ),
        migrations.AlterField(
            model_name='pasapp',
            name='signature_scan',
            field=models.ImageField(default='1', upload_to='signature_scans/', verbose_name='Скан подписи'),
        ),
    ]
