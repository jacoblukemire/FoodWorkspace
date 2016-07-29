from django.shortcuts import render
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from food.models import UserProfile, FoodItem, DataEntry
from food.forms import FoodItemForm, FoodEntryForm


def index(request):

    # Query the database for a list of ALL categories currently stored.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    foodItem_list = FoodItem.objects.all()
    profile = UserProfile.objects.all() # This will need to become the specific profile
    entries = DataEntry.objects.all() # This will need to be TODAYs entries for that profile

    today_calories = 0
    today_calories_from_fat = 0
    today_total_fat = 0
    today_saturated_fat = 0
    today_trans_fat = 0
    today_cholesterol = 0
    today_sodium = 0
    today_total_carbohydrate = 0
    today_dietary_fiber = 0
    today_sugars = 0
    today_protein = 0

    recommended_calories = {
        'amount': 2000,
        'unit': 'calories'
    }
    recommended_calories_from_fat = {
        'amount': 550,
        'unit': 'calories'
    }

    recommended_total_fat = {
        'amount': 65,
        'unit': 'grams'
    }
    recommended_saturated_fat = {
        'amount': 20,
        'unit': 'grams'
    }
    recommended_trans_fat = {
        'amount': 2,
        'unit': 'grams'
    }
    recommended_cholesterol = {
        'amount': 300,
        'unit': 'milligrams'
    }
    recommended_sodium = {
        'amount': 2400,
        'unit': 'milligrams'
    }
    recommended_total_carbohydrate = {
        'amount': 300,
        'unit': 'grams'
    }
    recommended_dietary_fiber = {
        'amount': 25,
        'unit': 'grams'
    }
    recommended_sugars = {
        'amount': 36,
        'unit': 'grams'
    }
    recommended_protein = {
        'amount': 50,
        'unit': 'grams'
    }

    for e in entries:
        if e.date_of_consumption == date.today():
            if e.user == request.user:
                name = e.entry_item
                quantity = e.quantity
                entry_food = FoodItem.objects.get(name=name)
                today_calories += entry_food.calories * quantity
                today_calories_from_fat += entry_food.calories_from_fat * quantity
                today_total_fat += entry_food.total_fat * quantity
                today_saturated_fat += entry_food.saturated_fat * quantity
                today_trans_fat += entry_food.trans_fat * quantity
                today_cholesterol += entry_food.cholesterol * quantity
                today_sodium += entry_food.sodium * quantity
                today_total_carbohydrate += entry_food.total_carbohydrate * quantity
                today_dietary_fiber += entry_food.dietary_fiber * quantity
                today_sugars += entry_food.sugars * quantity
                today_protein += entry_food.protein * quantity

    def adjust_percent(today, recommended):
        percent = 100 * today / recommended
        if percent > 100:
            return 100
        else:
            return percent

    calories_dict = {
        'today': today_calories,
        'recommended': recommended_calories,
        'percent': 100 * today_calories / recommended_calories['amount'],
        'adjusted_percent': adjust_percent(today_calories, recommended_calories['amount'])
    }

    calories_from_fat_dict = {
        'today': today_calories_from_fat,
        'recommended': recommended_calories_from_fat,
        'percent': 100 * today_calories_from_fat / recommended_calories_from_fat['amount'],
        'adjusted_percent': adjust_percent(today_calories_from_fat, recommended_calories_from_fat['amount'])
    }

    total_fat_dict = {
        'today': today_total_fat,
        'recommended': recommended_total_fat,
        'percent': 100 * today_total_fat / recommended_total_fat['amount'],
        'adjusted_percent': adjust_percent(today_total_fat, recommended_total_fat['amount'])
    }

    saturated_fat_dict = {
        'today': today_saturated_fat,
        'recommended': recommended_saturated_fat,
        'percent': 100 * today_saturated_fat / recommended_saturated_fat['amount'],
        'adjusted_percent': adjust_percent(today_saturated_fat, recommended_saturated_fat['amount'])
    }

    trans_fat_dict = {
        'today': today_trans_fat,
        'recommended': recommended_trans_fat,
        'percent': 100 * today_trans_fat / recommended_trans_fat['amount'],
        'adjusted_percent': adjust_percent(today_trans_fat, recommended_trans_fat['amount'])
    }

    cholesterol_dict = {
        'today': today_cholesterol,
        'recommended': recommended_cholesterol,
        'percent': 100 * today_cholesterol / recommended_cholesterol['amount'],
        'adjusted_percent': adjust_percent(today_cholesterol, recommended_cholesterol['amount'])
    }

    sodium_dict = {
        'today': today_sodium,
        'recommended': recommended_sodium,
        'percent': 100 * today_sodium / recommended_sodium['amount'],
        'adjusted_percent': adjust_percent(today_sodium, recommended_sodium['amount'])
    }

    total_carbohydrate_dict = {
        'today': today_total_carbohydrate,
        'recommended': recommended_total_carbohydrate,
        'percent': 100 * today_total_carbohydrate / recommended_total_carbohydrate['amount'],
        'adjusted_percent': adjust_percent(today_total_carbohydrate, recommended_total_carbohydrate['amount'])
    }

    dietary_fiber_dict = {
        'today': today_dietary_fiber,
        'recommended': recommended_dietary_fiber,
        'percent': 100 * today_dietary_fiber / recommended_dietary_fiber['amount'],
        'adjusted_percent': adjust_percent(today_dietary_fiber, recommended_dietary_fiber['amount'])
    }

    sugars_dict = {
        'today': today_sugars,
        'recommended': recommended_sugars,
        'percent': 100 * today_sugars / recommended_sugars['amount'],
        'adjusted_percent': adjust_percent(today_sugars, recommended_sugars['amount'])
    }

    protein_dict = {
        'today': today_protein,
        'recommended': recommended_protein,
        'percent': 100 * today_protein / recommended_protein['amount'],
        'adjusted_percent': adjust_percent(today_protein, recommended_protein['amount'])
    }

    context_dict = {'foodItems': foodItem_list,
                    'profile': profile,
                    'entries': entries,
                    'calories_dict': calories_dict,
                    'calories_from_fat_dict': calories_from_fat_dict,
                    'total_fat_dict': total_fat_dict,
                    'saturated_fat_dict': saturated_fat_dict,
                    'trans_fat_dict': trans_fat_dict,
                    'cholesterol_dict': cholesterol_dict,
                    'sodium_dict': sodium_dict,
                    'total_carbohydrate_dict': total_carbohydrate_dict,
                    'dietary_fiber_dict': dietary_fiber_dict,
                    'sugars_dict': sugars_dict,
                    'protein_dict': protein_dict
                    }

    # Render the response and send it back!
    return render(request, 'food/index.html', context_dict)


def view_foodlog(request):
    pass

    # # Query the database for a list of ALL categories currently stored.
    # # Place the list in our context_dict dictionary which will be passed to the template engine.
    # foodItem_list = FoodItem.objects.all()
    # profile = UserProfile.objects.all() # This will need to become the specific profile
    # entries = DataEntry.objects.all() # This will need to be TODAYs entries for that profile
    #
    # today_calories = 0
    # today_calories_from_fat = 0
    # today_total_fat = 0
    # today_saturated_fat = 0
    # today_trans_fat = 0
    # today_cholesterol = 0
    # today_sodium = 0
    # today_total_carbohydrate = 0
    # today_dietary_fiber = 0
    # today_sugars = 0
    # today_protein = 0
    # objects_iterated = 0
    #
    # for e in entries:
    #     name = e.entry_item
    #     quantity = e.quantity
    #     entry_food = FoodItem.objects.get(name=name)
    #     today_calories += entry_food.calories * quantity
    #     today_calories_from_fat += entry_food.calories_from_fat * quantity
    #     today_total_fat += entry_food.total_fat * quantity
    #     today_saturated_fat += entry_food.saturated_fat * quantity
    #     today_trans_fat += entry_food.trans_fat * quantity
    #     today_cholesterol += entry_food.cholesterol * quantity
    #     today_sodium += entry_food.sodium * quantity
    #     today_total_carbohydrate += entry_food.total_carbohydrate * quantity
    #     today_dietary_fiber += entry_food.dietary_fiber * quantity
    #     today_sugars += entry_food.sugars * quantity
    #     today_protein += entry_food.protein * quantity
    #
    #     # Test variables
    #     date_eaten = e.date_of_consumption
    #     objects_iterated += 1
    #
    # context_dict = {'foodItems': foodItem_list,
    #                 'profile': profile,
    #                 'entries': entries,
    #                 'today_calories': today_calories,
    #                 'today_calories_from_fat': today_calories_from_fat,
    #                 'today_total_fat': today_total_fat,
    #                 'today_saturated_fat': today_saturated_fat,
    #                 'today_trans_fat': today_trans_fat,
    #                 'today_cholesterol': today_cholesterol,
    #                 'today_sodium': today_sodium,
    #                 'today_total_carbohydrate': today_total_carbohydrate,
    #                 'today_dietary_fiber': today_dietary_fiber,
    #                 'today_sugars': today_sugars,
    #                 'today_protein': today_protein,
    #                 'date_eaten': date_eaten,
    #                 'objects_iterated': objects_iterated,
    #                 }
    #
    # # Render the response and send it back!
    # return render(request, 'food/food_log.html', context_dict)


def add_fooditem(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = FoodItemForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            save_it = form.save(commit = False)
            save_it.user = request.user
            save_it.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = FoodItemForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'food/add_fooditem.html', {'form': form})


def add_foodentry(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.cleaned_data
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = FoodEntryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'food/add_foodentry.html', {'form': form})


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
