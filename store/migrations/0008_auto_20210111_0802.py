# Generated by Django 3.0.8 on 2021-01-11 02:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210111_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 11, 8, 2, 6, 155293)),
        ),
    ]
