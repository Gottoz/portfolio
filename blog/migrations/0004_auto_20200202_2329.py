# Generated by Django 2.0.2 on 2020-02-02 23:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 2, 23, 29, 36, 249606, tzinfo=utc)),
        ),
    ]
