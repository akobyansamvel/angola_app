# Generated by Django 5.0.6 on 2024-06-07 19:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passport', '0002_passport_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ожидание', 'Ожидание'), ('подтверждено', 'Подтверждено'), ('отменено', 'Отменено')], default='ожидание', max_length=15, verbose_name='Статус')),
                ('passport_data', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='passport_estate', to='passport.passport')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
