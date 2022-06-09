from django.shortcuts import render

from tourism.models import Place

# Create your views here.

def home(requests):
    place1 = Place()
    place1.name = 'Turkana'
    place1.date = '6 June 2022'
    place1.img = '1.jpg'
    place1.desc = 'The oil rich city. Has the largest desert lake. Rich culture also'
    place1.posts = 'Victor'

    place2 = Place()
    place2.date = '8 June 2022'
    place2.img = 'Amazing.jpg'
    place2.desc = 'The city in the mountains. The industrial city. Nice views. Lovely'
    place2.name = 'Isiolo'
    place2.posts = 'Waburi'

    places = [place1, place2]


    return render(requests, 'home.html', {'places' : places})