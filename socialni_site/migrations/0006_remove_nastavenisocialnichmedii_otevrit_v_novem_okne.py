# Generated by Django 3.1.4 on 2021-01-17 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialni_site', '0005_auto_20210117_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nastavenisocialnichmedii',
            name='otevrit_v_novem_okne',
        ),
    ]