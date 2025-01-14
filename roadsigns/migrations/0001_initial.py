# Generated by Django 5.0.4 on 2024-05-25 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='all/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='all/videos')),
                ('audio', models.FileField(blank=True, null=True, upload_to='all/audios')),
                ('docs', models.FileField(blank=True, null=True, upload_to='all/docs')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadsigns.categories')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]
