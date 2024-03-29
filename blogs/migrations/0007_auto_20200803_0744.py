# Generated by Django 3.0.8 on 2020-08-03 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200803_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='author_email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author_name',
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 3, 7, 44, 40, 820190)),
        ),
    ]
