# Generated by Django 5.0.6 on 2024-06-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamFarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('program_name', models.CharField(max_length=255, verbose_name='Название программы')),
                ('project_name', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('project_location', models.CharField(max_length=255, verbose_name='Локация проекта')),
                ('project_description', models.TextField(verbose_name='Описание проекта')),
                ('applicant_full_name', models.CharField(max_length=255, verbose_name='ФИО заявителя')),
                ('applicant_address', models.CharField(max_length=255, verbose_name='Адрес заявителя')),
                ('applicant_zip_code', models.CharField(max_length=10, verbose_name='Индекс заявителя')),
                ('applicant_city', models.CharField(max_length=100, verbose_name='Город заявителя')),
                ('applicant_phone', models.CharField(max_length=20, verbose_name='Телефон заявителя')),
                ('applicant_email', models.EmailField(max_length=254, verbose_name='Email заявителя')),
                ('applicant_website', models.URLField(blank=True, null=True, verbose_name='Сайт заявителя')),
                ('organization_type', models.CharField(choices=[('ИП', 'Индивидуальный предприниматель'), ('ООО', 'Общество с ограниченной ответственностью'), ('Фермерское хозяйство', 'Фермерское хозяйство'), ('Другое', 'Другое')], max_length=50, verbose_name='Тип организации')),
                ('partner_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название партнёра')),
                ('partner_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес партнёра')),
                ('partner_zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Индекс партнёра')),
                ('partner_city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город партнёра')),
                ('partner_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон партнёра')),
                ('partner_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email партнёра')),
                ('partner_website', models.URLField(blank=True, null=True, verbose_name='Сайт партнёра')),
            ],
            options={
                'verbose_name': 'Поддержка семейного фермерства',
                'verbose_name_plural': 'Поддержка семейного фермерства',
            },
        ),
    ]
