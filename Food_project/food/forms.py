from django import forms
from django.forms import formset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from food.models import UserProfile, FoodItem, DataEntry

class FoodItemForm(forms.ModelForm):
    # This form needs all of the different attributes
    # I will want one form for new full item and one for new combination item????????????
    name = forms.CharField(max_length=128, help_text="Please enter the food name. I should make this a search box.")
    food_group = forms.CharField(max_length=128, help_text="Food Group:")
    calories = forms.IntegerField(help_text="Calories:")
    calories_from_fat = forms.IntegerField(help_text="Calories From Fat:")
    total_fat = forms.IntegerField(help_text="Total Fat:")
    saturated_fat = forms.IntegerField(help_text="Saturated Fat:")
    trans_fat = forms.IntegerField(help_text="Trans Fat:")
    cholesterol = forms.IntegerField(help_text="Cholesterol:")
    sodium = forms.IntegerField(help_text="Sodium:")
    total_carbohydrate = forms.IntegerField(help_text="Total Carbohydrate:")
    dietary_fiber = forms.IntegerField(help_text="Dietary Fiber:")
    sugars = forms.IntegerField(help_text="Sugars:")
    protein = forms.IntegerField(help_text="Protein:")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = FoodItem
        fields = ('name', 'food_group', 'calories', 'calories_from_fat', 'total_fat', 'saturated_fat',
                  'trans_fat', 'cholesterol', 'sodium', 'total_carbohydrate', 'dietary_fiber', 'sugars', 'protein')

class FoodEntryForm(forms.ModelForm):
    # This form needs all of the different attributes
    # I will want one form for new full item and one for new combination item????????????
    # entry_id = forms.IntegerField(help_text="Entry ID. I need to get rid of this")
    # user = forms.CharField(max_length=128, help_text="User. I need to get rid of this.")
    user = User
    entry_item = forms.CharField(max_length=128, help_text="Please enter the food name. Should be search box.")
    quantity = forms.IntegerField(help_text="Quantity:")

    def clean(self):
        self.user = User

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = DataEntry
        fields = ('user', 'entry_item', 'quantity')


# This form will be nested inside of the FoodRecipeForm, the difference being FoodRecipeForm contains the user
# As well as many instances of FoodRecipePiece
class FoodRecipePiece(forms.ModelForm):
    entry_item = forms.CharField(max_length=128, help_text="Please enter the food name. Should be search box.")
    quantity = forms.IntegerField(help_text="Quantity:")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = DataEntry
        fields = ('entry_item', 'quantity')


class FoodRecipeForm(forms.ModelForm):
    # I want a formset - see tutorial by someone named like nicole
    user = User

    def clean(self):
        self.user = User

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = DataEntry
        fields = ('user', 'entry_item', 'quantity')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'height', 'weight', 'age')
