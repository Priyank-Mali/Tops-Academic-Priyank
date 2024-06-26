# Generated by Django 5.0.6 on 2024-06-27 08:38

import django.db.models.deletion
import master.utils.TA_UNIQUE.filename
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_productbrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='master.basemodel')),
                ('model_name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to=master.utils.TA_UNIQUE.filename.generate_unique_filename)),
                ('ram', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.productbrand')),
            ],
            options={
                'unique_together': {('company', 'model_name')},
            },
            bases=('master.basemodel',),
        ),
    ]
