# Generated by Django 5.0.6 on 2024-06-21 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_technology_batch'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.batch')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
