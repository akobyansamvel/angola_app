# Generated by Django 5.0.6 on 2024-06-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyFarmingSupport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='famfarm',
            name='status',
            field=models.CharField(choices=[('ожидание', 'Ожидание'), ('подтверждено', 'Подтверждено'), ('отменено', 'Отменено')], default='ожидание', max_length=15, verbose_name='Статус'),
        ),
    ]