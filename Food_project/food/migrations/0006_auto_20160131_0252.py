# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20160131_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataentry',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=128),
        ),
    ]
