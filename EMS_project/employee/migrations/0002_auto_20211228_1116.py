# Generated by Django 3.2 on 2021-12-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
