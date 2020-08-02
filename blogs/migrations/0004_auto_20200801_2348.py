# Generated by Django 3.0.8 on 2020-08-01 18:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200801_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 1, 23, 48, 27, 914829)),
        ),
    ]