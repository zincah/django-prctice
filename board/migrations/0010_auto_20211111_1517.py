# Generated by Django 3.2.8 on 2021-11-11 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_alter_reply_pubdate2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='pubdate2',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 11, 15, 17, 17, 546448)),
        ),
        migrations.DeleteModel(
            name='Scrap',
        ),
    ]
