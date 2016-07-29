# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_id', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('food_group', models.CharField(max_length=128)),
                ('calories', models.IntegerField(default=0)),
                ('calories_from_fat', models.IntegerField(default=0)),
                ('total_fat', models.IntegerField(default=0)),
                ('saturated_fat', models.IntegerField(default=0)),
                ('trans_fat', models.IntegerField(default=0)),
                ('cholesterol', models.IntegerField(default=0)),
                ('sodium', models.IntegerField(default=0)),
                ('total_carbohydrate', models.IntegerField(default=0)),
                ('dietary_fiber', models.IntegerField(default=0)),
                ('sugars', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='entry_item',
            field=models.ForeignKey(to='food.FoodItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataentry',
            name='user',
            field=models.ForeignKey(to='food.Profile'),
            preserve_default=True,
        ),
    ]
