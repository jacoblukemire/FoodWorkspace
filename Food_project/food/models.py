from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username


class FoodItem(models.Model):
    # category = models.ForeignKey(Category)
    # title = models.CharField(max_length=128)
    # url = models.URLField()
    # views = models.IntegerField(default=0)
    name = models.CharField(max_length=128)
    food_group = models.CharField(max_length=128)
    calories = models.IntegerField(default=0)
    calories_from_fat = models.IntegerField(default=0)
    total_fat = models.IntegerField(default=0)
    saturated_fat = models.IntegerField(default=0)
    trans_fat = models.IntegerField(default=0)
    cholesterol = models.IntegerField(default=0)
    sodium = models.IntegerField(default=0)
    total_carbohydrate = models.IntegerField(default=0)
    dietary_fiber = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class DataEntry(models.Model):
    user = models.ForeignKey(User)
    entry_item = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    date_of_consumption = models.DateField(default=date.today())

    def __unicode__(self):
        return str(self.entry_id)
