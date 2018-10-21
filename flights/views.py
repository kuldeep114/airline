from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passengers

# Create your views here.


def index(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, "flights/index.html", context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight Does not Exist")
    context = {
        "flight": flight,
        # "passengers": flight.Passengers.all()
    }
    return render(request, "flights/flight.html", context)


def book(request, flight_id):
    try:
        passenger_id = int(request.Post["passenger"])
        passenger = Passengers.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        render(request, "flights.error.html", {"message": "No Selection"})
    except Flight.DoesNotExist:
        render(request, "flights.error.html", {"message": "No Flight"})
    except Passengers.DoesNotExist:
        render(request, "flights.error.html", {"message": "No Passenger"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id)))
