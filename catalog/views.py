from django.shortcuts import render

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

