# Generated by Django 3.2.8 on 2021-11-16 04:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20211111_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='pubdate2',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 13, 2, 52, 581368)),
        ),
    ]
