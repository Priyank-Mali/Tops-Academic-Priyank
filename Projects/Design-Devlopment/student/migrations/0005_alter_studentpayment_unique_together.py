# Generated by Django 5.0.6 on 2024-06-24 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('student', '0004_studentpayment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentpayment',
            unique_together={('student_id', 'technology_id')},
        ),
    ]
