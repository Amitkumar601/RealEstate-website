from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,bedroom_choices,price_choices
# Create your views here.
def index(request):
    latest_listings=Listing.objects.all()[:3]
    context={
    'latest_listings':latest_listings,
    'state_choices':state_choices,
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices
    }
    return render(request,'pages/index.html',context)
def about(request):
    realtors = Realtor.objects.all()
    context={
        'realtors':realtors
    }
    
    return render(request, 'pages/about.html',context)
