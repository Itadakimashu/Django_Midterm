# Generated by Django 4.2.1 on 2024-07-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('instrument_type', models.CharField(choices=[('Guitar', 'Guitar'), ('Drums', 'Drums'), ('Bass', 'Bass'), ('Keyboard', 'Keyboard')], max_length=100)),
            ],
        ),
    ]