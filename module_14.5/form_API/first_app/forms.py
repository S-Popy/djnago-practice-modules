from django import forms 
from django.forms.widgets import NumberInput
import datetime
from django.core import validators



BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

FAVORITE_SPORTS_CHOICES = [
    ('cricket', 'Cricket'),
    ('football', 'FootBall'),
    ('basketball', 'BasketBall'),
]


class ExampleForm(forms.Form):
    name = forms.CharField(max_length = 30, label = "Full Name", validators =[validators.MinLengthValidator(10, message = "Enter a name with at least 10 characters")])

    email = forms.EmailField(initial = "abc@gmail.com")

    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    
    password = forms.CharField(widget = forms.PasswordInput()) 

    date = forms.DateField(required = False,initial=datetime.date.today)

    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    value = forms.DecimalField()

    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_sports = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_SPORTS_CHOICES,)

    message = forms.CharField(widget=forms.Textarea, label = "Write Your message", required = False)

    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required = False)

    agree = forms.BooleanField(initial=True)