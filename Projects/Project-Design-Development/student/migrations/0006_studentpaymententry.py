# Generated by Django 5.0.6 on 2024-07-15 09:46

import django.db.models.deletion
import master.utils.TA_UNIQE.uniques_filename
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studentpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPaymentEntry',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('proof', models.ImageField(upload_to=master.utils.TA_UNIQE.uniques_filename.generate_unique_filename)),
                ('paid_date', models.DateField()),
                ('installment', models.FloatField(default=Decimal('0.00'))),
                ('stdent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
