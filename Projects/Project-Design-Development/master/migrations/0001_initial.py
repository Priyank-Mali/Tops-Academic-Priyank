# Generated by Django 5.0.6 on 2024-06-23 10:17

import master.utils.TA_UNIQE.uniques_filename
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('technology_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=master.utils.TA_UNIQE.uniques_filename.generate_unique_filename)),
                ('fees', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]