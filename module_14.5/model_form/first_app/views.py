from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            form = ExampleForm()
    else:
        form = ExampleForm()
    return render(request, 'first_app/home.html', {'form' : form})