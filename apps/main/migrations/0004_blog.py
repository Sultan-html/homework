# Generated by Django 5.1.2 on 2024-10-24 15:36

import apps.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_artist_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.utils.custom_upload_path, verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Запись блога',
                'verbose_name_plural': 'Записи блога',
            },
        ),
    ]
