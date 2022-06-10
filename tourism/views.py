from django.shortcuts import render

from tourism.models import Place


# Create your views here.

def home(requests):
    
    places = Place.objects.all()
    


    return render(requests, 'home.html', {'places' : places})