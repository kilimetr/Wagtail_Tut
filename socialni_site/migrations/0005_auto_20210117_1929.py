# Generated by Django 3.1.4 on 2021-01-17 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialni_site', '0004_nastavenisocialnichmedii_open_in_new_tab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nastavenisocialnichmedii',
            old_name='open_in_new_tab',
            new_name='otevrit_v_novem_okne',
        ),
    ]