# Generated by Django 3.0.3 on 2020-02-27 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200227_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='faculty_id',
        ),
    ]
