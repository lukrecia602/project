# Generated by Django 5.1.2 on 2024-12-09 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('penzvalto', '0002_valutak_penznemhosszan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valutak',
            name='penznemhosszan',
        ),
    ]
