# Generated by Django 5.0.6 on 2024-06-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceApplication', '0008_alter_insapp_passport_scan_alter_insapp_recipient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insapp',
            name='passport_scan',
            field=models.ImageField(null=True, upload_to='passport_scans/', verbose_name='Скан паспорта'),
        ),
    ]
