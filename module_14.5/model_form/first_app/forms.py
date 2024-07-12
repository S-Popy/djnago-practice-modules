from .models import ExampleModel
from django import forms
from django.forms.widgets import NumberInput


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel 
        fields = ['id', 'name', 'email', 'roll', 'mobile_number', 'passed', 'date', 'birth_date', 'class_length', 'fees', 'comments']

        labels = {

            'class_length' :'Class Duration',
        }
        

        help_texts = {
            'name':'Enter Your full name', 'mobile_number':'Please include country code'
        }

        widgets = {
            'password' : forms.PasswordInput(),
            'birth_date' : NumberInput(attrs={'type': 'date'})
        }
        
