from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight_view(request, id):
    flight = Flight.objects.get(pk=id)
    return render(request, "flights/flight.html", {
        "flight": flight, "passengers": flight.passengers.all(), "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book_view(request, id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=id)
        passenger = Passenger.objects.get(pk=request.POST['passenger'])
        passenger.flights.add(flight)
        # return HttpResponseRedirect(reverse("flight", args=[id]))
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    else:
        return render(request, "flights/book.html")