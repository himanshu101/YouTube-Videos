# Generated by Django 3.0.8 on 2020-07-05 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_mysql.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('thumbnails', jsonfield.fields.JSONField(default=dict, help_text='Storing thumbnails for videos')),
                ('source', django_mysql.models.EnumField(choices=[('YOUTUBE', 'YOUTUBE')], db_index=True, default='YOUTUBE')),
                ('video_id', models.CharField(max_length=200, null=True)),
                ('published_at', models.DateTimeField(default=datetime.datetime(2020, 7, 5, 16, 52, 23, 77368, tzinfo=utc))),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
