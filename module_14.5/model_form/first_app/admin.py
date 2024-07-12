from django.contrib import admin
from .models import ExampleModel 

# Register your models here.
@admin.register(ExampleModel)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'roll', 'mobile_number', 'birth_date', 'fees']
