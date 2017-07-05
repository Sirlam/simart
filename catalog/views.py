from django.shortcuts import render

from django.views import generic

# Create your views here.

from .models import Station, TankQuantity, PumpSale, OnAccountSale


def index(request):
    """
    View function for the home page site
    """
    # TODO: Generate station name

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )


class StationListView(generic.ListView):
    model = Station
    queryset = Station.objects.all()  # Get all stations
    context_object_name = 'my_station_list'  # your own name for the list as a template variable
    template_name = 'station_list.html'  # Specify your own template name/location


