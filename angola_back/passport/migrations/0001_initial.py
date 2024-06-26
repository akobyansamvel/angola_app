# Generated by Django 5.0.6 on 2024-05-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('citizenship', models.CharField(max_length=100, verbose_name='Гражданство')),
                ('series_number', models.CharField(max_length=20, verbose_name='Серия и номер')),
                ('issued_by', models.CharField(max_length=200, verbose_name='Кем выдан')),
                ('issued_date', models.DateField(verbose_name='Дата выдачи')),
                ('expiry_date', models.DateField(verbose_name='Срок действия')),
            ],
        ),
    ]
