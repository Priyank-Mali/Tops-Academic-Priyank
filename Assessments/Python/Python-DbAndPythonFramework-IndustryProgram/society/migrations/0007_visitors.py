# Generated by Django 5.0.6 on 2024-07-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0006_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]