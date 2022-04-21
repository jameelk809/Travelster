from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, then Sherwani'
    dest2.price = 650
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'Beautiful city'
    dest3.price = 600
    dest3.img = 'destination_3.jpg'

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
