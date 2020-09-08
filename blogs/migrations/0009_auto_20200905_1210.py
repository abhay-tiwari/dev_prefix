# Generated by Django 3.0.8 on 2020-09-05 06:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20200905_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blogs.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 5, 12, 10, 26, 53806)),
        ),
    ]
