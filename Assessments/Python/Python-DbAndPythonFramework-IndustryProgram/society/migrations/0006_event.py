# Generated by Django 5.0.6 on 2024-06-30 09:54

import master.utils.TA_UNIQUE.filename
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0005_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_topic', models.CharField(max_length=255)),
                ('event_description', models.TextField()),
                ('image', models.FileField(upload_to=master.utils.TA_UNIQUE.filename.generate_unique_filename)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
