# Generated by Django 3.0.8 on 2020-08-02 12:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20200801_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 2, 18, 7, 19, 418581)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.Blog')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]