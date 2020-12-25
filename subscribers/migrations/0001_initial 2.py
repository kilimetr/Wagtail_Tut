# Generated by Django 3.1.4 on 2020-12-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='Email Address', max_length=100)),
                ('full_name', models.CharField(help_text='First and last name', max_length=100)),
            ],
        ),
    ]
