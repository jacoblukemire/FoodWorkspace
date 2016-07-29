import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Food_project.settings')

import django
from datetime import date
django.setup()

from food.models import UserProfile, FoodItem, DataEntry


def populate():

    # add_profile('Test Profile', 'Jacob Lukemire', 68, 140, 18)

    add_food('egg', 'meat', 78, 47, 5, 2, 0, 187, 62, 1, 0, 1, 6)
    add_food('oven-roasted chicken breast (3 slices)', 'meat', 35, 20, 2, 1, 0, 12, 295, 0, 0, 0, 8)
    add_food('mayonaise', 'condiment', 94, 11, 10, 2, 0, 6, 88, 0, 0, 0, 0)
    add_food('bread (whole-wheat) (1 slice)', 'bread', 69, 0, 1, 0, 0, 0, 112, 12, 2, 2, 4)

    # add_entry('Test Profile', 'test chicken', 3, date.today())
    # add_entry('Test Profile', 'test apple', 3, date.today())

    # Print out what we have added to the user.
    #for p in UserProfile.objects.all():
    #    print p
    for f in FoodItem.objects.all():
        print f


def add_profile(username, name, height, weight, age):
    p = UserProfile.objects.get_or_create(username=username, name=name, height=height, weight=weight, age=age)[0]
    p.save()
    return p


def add_food(name, food_group, calories, calories_from_fat, total_fat, saturated_fat, trans_fat, cholesterol, sodium,
             total_carbohydrate, dietary_fiber, sugars, protein):
    f = FoodItem.objects.get_or_create(name=name, food_group=food_group, calories=calories,
                                       calories_from_fat=calories_from_fat, total_fat=total_fat,
                                       saturated_fat=saturated_fat, trans_fat=trans_fat, cholesterol=cholesterol,
                                       sodium=sodium, total_carbohydrate=total_carbohydrate,
                                       dietary_fiber=dietary_fiber, sugars=sugars, protein=protein)[0]
    return f


def add_entry(user, entry_item, quantity, date_of_consumption):
    e = DataEntry.objects.get_or_create(user=user, entry_item=entry_item, quantity=quantity,
                                        date_of_consumption=date_of_consumption)[0]
    return e

# Start execution here!
if __name__ == '__main__':
    print "Starting Food population script..."
    populate()
