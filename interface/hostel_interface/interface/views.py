from django.shortcuts import render
from .models import *
# Create your views here.
from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponseNotFound
import random
from datetime import date


def index(request):
    return render(request, 'index.html')

def add_booking(request):
    placetype = PlaceType.objects.all()

    if request.method == 'POST':
        booking = Bookings()
        place = Places()
        guest = Guests()

        guest.name = request.POST.get("name")
        guest.surname = request.POST.get("surname")
        guest.fathername = request.POST.get("fathername")
        guest.passport = request.POST.get("passport")
        guest.gender = request.POST.get("gender")
        guest.address = request.POST.get("address")
        datee = request.POST.get("birthdate").split('/')
        b_date = date(int(datee[2]), int(datee[1]), int(datee[0]))
        guest.birthdate = b_date
        guest.phone_number = request.POST.get("phonenumber")
        guest.email = request.POST.get("booking-email")
        guest.save()

        f = request.POST.get("arrival").split('/')
        l = request.POST.get("departure").split('/')
        f_date = date(int(f[2]), int(f[1]), int(f[0]))
        l_date = date(int(l[2]), int(l[1]), int(l[0]))
        booking.arrival_date = f_date
        booking.checkout_date = l_date
        booking.room_type = request.POST.get("room-type")

        delta = l_date - f_date
        price = PlaceType.objects.values().get(type=request.POST.get("room-type"))['PRICE']
        booking.money_total = price * delta.days

        booking.bk_id = BookingStatus.objects.only('bk_id').get(status="A")
        booking.guest_id = Guests.objects.latest('guest_id')
        booking.place_id = Places.objects.only('place_id').filter(place_type_id=PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type")), available=True)[0]
        booking.save()

        last_place = Bookings.objects.values().latest("place_id")['place_id_id']
        place = Places.objects.get(place_id=last_place)
        place.available = False
        place.save(update_fields=["available"])
    else:
        booking = Bookings()
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


def add_placetype(request):
    last_ptype_ind = PlaceType.objects.values().latest("place_type_id")['place_type_id']
    if request.method == "POST":
        ptype = PlaceType()
        ptype.place_type_id = last_ptype_ind + 1
        ptype.type = request.POST.get("ptype")
        ptype.PRICE = request.POST.get("ptype_price")
        ptype.save()
    else:
        ptype = PlaceType()
    return render(request, 'add-placetype.html')


def all_placetype(request):
    ptype_list = PlaceType.objects.all()
    return render(request, 'all-placetype.html', {
        "ptype_list": ptype_list
    })

def all_services(request):
    service_list = Services.objects.all()
    return render(request, 'all-services.html', {
        "service_list": service_list
    })


def add_service(request):
    if request.method == "POST":
        service = Services()
        last_service_ind = 0
        if Services.objects.all():
            last_service_ind = Services.objects.values().latest("service_id")['service_id']
        service.service_id = last_service_ind + 1
        service.price = request.POST.get("service-price")
        service.description = request.POST.get("service-description")
        service.save()
    else:
        service = Services()
    return render(request, 'add-service.html')


def del_customer(request, id):
    del_place = Bookings.objects.values().get(guest_id=id)['place_id_id']
    place = Places.objects.get(place_id=del_place)
    place.available = True
    place.save()
    customer_list = Guests.objects.all()
    delete_list = Guests.objects.get(guest_id=id)
    delete_list.delete()
    return render(request, 'all-customer.html',
                  {
                      'id': id,
                      'customer_list': customer_list
                  }
    )


def all_room(request):
    places_list = Places.objects.all()
    ptypes = PlaceType.objects.all()
    return render(request, 'all-rooms.html',
                  {
                      'places_list': places_list,
                      'ptypes': ptypes
                  }
    )


def add_room(request):
    placetype = PlaceType.objects.all()
    if request.method == 'POST':
        places = Places()
        last_place = Places.objects.values().latest("place_id")['place_id']
        places.place_id = last_place + 1
        places.place_type_id = PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type"))
        places.available = True
        places.save()
    else:
        places = Places()

    return render(request, 'add-room.html', {
        'placetype':placetype
    })


def all_booking(request):
    booking_list = Bookings.objects.all()
    print("ALL BOOKING:", booking_list)
    return render(request, 'all-booking.html',
                  {
                      'booking_list': booking_list
                  }
    )

# -- Бронирования гостя за этот год
# select * from bookings where GUEST_ID = (SELECT GUEST_ID from guests limit 1);
# -- Количество бронирований в каждом хостеле
# select count(bookings.PB_ID) as bookings, hostels.* from hostels 
#   left join room on hostels.HOSTEL_ID = room.HOSTEL_ID
#   left join places on places.ROOM_ID = room.ROOM_ID 
#   left join bookings on bookings.PLACE_ID = places.PLACE_ID
# group by hostels.HOSTEL_ID
# order by count(bookings.PB_ID) desc;
# -- Количество мест в каждом хостеле
# select count(places.PLACE_ID) as places, hostels.* from hostels 
#   left join room on hostels.HOSTEL_ID = room.HOSTEL_ID
#   left join places on places.ROOM_ID = room.ROOM_ID 
# group by hostels.HOSTEL_ID
# order by count(places.PLACE_ID) desc;
# -- Какие типы комнат есть в хостеле
# select p.place_id, pt.type from places p, hostels h, room r, place_type pt where(p.room_id = r.room_id) and (h.hostel_id = r.hostel_id);
# -- Активные заказы в хостеле
# select b.pb_id from bookings b , booking_status bs where (b.bk_id = bs.bk_id) and (bs.status = 'C');
def get_reviews(request):
    booking_list = Bookings.objects.raw('select * from interface_bookings where money_total > 1000')
    print("ALL BOOKING:", booking_list)
    return render(request, 'reviews.html',
        {
            'booking_list': booking_list
        }
    )


def edit_customer(request, id):
    g_edit = Guests.objects.get(guest_id=id)
    b_edit = Bookings.objects.get(guest_id=id)
    placetype = PlaceType.objects.all()
    if request.method == 'POST':
        booking = Bookings.objects.get(guest_id=id)
        guest = Guests.objects.get(guest_id=id)

        guest.name = request.POST.get("name")
        guest.surname = request.POST.get("surname")
        guest.fathername = request.POST.get("fathername")
        guest.passport = request.POST.get("passport")
        guest.gender = request.POST.get("gender")
        guest.address = request.POST.get("address")
        guest.birthdate = request.POST.get("birthdate")
        guest.phone_number = request.POST.get("phonenumber")
        guest.email = request.POST.get("booking-email")
        guest.save()
        booking.arrival_date = request.POST.get("arrival")
        booking.checkout_date = request.POST.get("departure")
        booking.room_type = request.POST.get("room-type")

        f = request.POST.get("arrival").split('/')
        l = request.POST.get("departure").split('/')
        f_date = date(int(f[2]), int(f[1]), int(f[0]))
        l_date = date(int(l[2]), int(l[1]), int(l[0]))
        delta = l_date - f_date
        booking.money_total = 1000 * delta.days if request.POST.get("room-type") == 'Single' else 1600 * delta.days

        booking.bk_id = BookingStatus.objects.only('bk_id').get(status="A")
        booking.guest_id = Guests.objects.get(guest_id=id)
        booking.place_id = Places.objects.only('place_id').filter(place_type_id=PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type")), available=True)[0]
        booking.save()

        print("ADD BOOKING:", request)
    return render(request, 'edit-customer.html',
                  {
                      'id': id,
                      'g_edit': g_edit,
                      'b_edit': b_edit,
                      'placetype': placetype
                  }
    )
