# Generated by Django 3.1.4 on 2021-01-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialni_site', '0003_auto_20210117_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='nastavenisocialnichmedii',
            name='open_in_new_tab',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
