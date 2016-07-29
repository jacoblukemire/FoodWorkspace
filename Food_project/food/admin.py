from django.contrib import admin
from food.models import UserProfile, FoodItem, DataEntry


# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# When I add a MODEL, it needs to be added here in order to appear in the admin
admin.site.register(UserProfile)
admin.site.register(FoodItem)
admin.site.register(DataEntry)
