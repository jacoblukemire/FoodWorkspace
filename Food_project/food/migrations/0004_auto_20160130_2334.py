# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20160122_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataentry',
            name='entry_id',
        ),
        migrations.AddField(
            model_name='dataentry',
            name='date_of_consumption',
            field=models.DateField(default=datetime.date(2016, 1, 30)),
            preserve_default=True,
        ),
    ]
