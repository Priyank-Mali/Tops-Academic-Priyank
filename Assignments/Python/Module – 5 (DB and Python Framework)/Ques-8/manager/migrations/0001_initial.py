# Generated by Django 5.0.6 on 2024-06-27 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0002_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('information_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='master.information')),
                ('manager_id', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=255)),
            ],
            bases=('master.information',),
        ),
    ]
