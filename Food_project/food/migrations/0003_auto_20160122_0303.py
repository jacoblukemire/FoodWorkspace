# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20160122_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataentry',
            name='entry_item',
            field=models.CharField(max_length=128),
        ),
    ]
