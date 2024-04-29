from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    data = {'str_list' : ['python', 'is', 'fun'],
    'dict_list': [{'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
    ],
    'date' : datetime.datetime.now(),
    'value' : 5,
    'value2':"",
    'string' : "I'm Django",
    'string2' : 'python',
    'string3' : 'HELLO WORLD',
    'title' : 'django filters'
    }
    
    return render(request, 'index.html', data)
