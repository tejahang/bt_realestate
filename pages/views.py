from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor
# Create your views here.


def index(request):
    latest_listings = {
        'latests': Listing.objects.order_by('-list_date').filter(is_published=True)[:3],
        'bedroom_choices': bedroom_choices, 
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/index.html', latest_listings)


def about(request):
    realtors_list = {
        'realtors': Realtor.objects.all(),
        'mvp': Realtor.objects.all().filter(is_mvp=True)
    }
    return render(request, 'pages/about.html', realtors_list)
