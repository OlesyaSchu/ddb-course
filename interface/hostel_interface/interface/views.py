from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound
import random

def index(request):
    return render(request, 'index.html')


def add_booking(request):
    placetype = PlaceType.objects.all()
    if request.method == 'POST':
        # booking = Bookings()
        guest = Guests()
        guest.name = request.POST.get("name")
        guest.surname = request.POST.get("surname")
        guest.fathername = request.POST.get("fathername")
        guest.gender = request.POST.get("gender")
        guest.address = request.POST.get("address")
        guest.birthdate = request.POST.get("birthdate")
        guest.phone = request.POST.get("phone-number")
        guest.email = request.POST.get("booking-email")
        # booking.bk_id = random.randint(1, 100)
        # booking.arrival_date = request.POST.get("arrival")
        # booking.checkout_date = request.POST.get("departure")
        # booking.room_type = request.POST.get("room-type")
        # booking.money_total = 1000 # (placetype.price)
        # print("########", booking.checkout_date - booking.arrival_date)
        guest.save()
        # booking.save()
    else:
        # booking = Bookings()
        guest = Guests()


    return render(request, 'add-booking.html', {
        'placetype':placetype
    })

def all_customer(request):
    customer_list = Guests.objects.all()
    return render(request, 'all-customer.html',
                  {
                      'customer_list': customer_list
                  }
    )

def all_room(request):
    return render(request, 'all-rooms.html')

def add_room(request):
    return render(request, 'add-room.html')

def all_booking(request):
    booking_list = Bookings.objects.all()
    return render(request, 'all-booking.html',
                  {
                      'booking_list': booking_list
                  }
    )

