# Generated by Django 3.2.8 on 2021-11-10 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20211110_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='pubdate2',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 17, 46, 15, 315008)),
        ),
    ]