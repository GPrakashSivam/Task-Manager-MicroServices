# Generated by Django 5.1.3 on 2024-11-07 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
