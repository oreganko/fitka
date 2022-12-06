from django.contrib import admin

# Register your app_models here.
from .models import DietDay, DayMeals

admin.site.register(DietDay)
admin.site.register(DayMeals)
