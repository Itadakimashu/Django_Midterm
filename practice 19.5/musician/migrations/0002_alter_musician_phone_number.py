# Generated by Django 4.2.1 on 2024-07-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
