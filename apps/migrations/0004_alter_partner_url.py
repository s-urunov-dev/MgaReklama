# Generated by Django 5.2.1 on 2025-07-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_rename_icon_service_image_remove_service_hover_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='URL'),
        ),
    ]
