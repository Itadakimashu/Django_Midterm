# Generated by Django 4.2.1 on 2024-08-04 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Car',
            new_name='car',
        ),
    ]
