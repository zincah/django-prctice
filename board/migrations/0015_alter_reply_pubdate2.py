# Generated by Django 3.2.8 on 2021-11-16 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_alter_reply_pubdate2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='pubdate2',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 14, 38, 27, 173750)),
        ),
    ]