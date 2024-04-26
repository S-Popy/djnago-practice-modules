from django.shortcuts import render

# Create your views here.
def home(request):
    data = [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]
    return render(request, 'index.html', {'data' : data})
