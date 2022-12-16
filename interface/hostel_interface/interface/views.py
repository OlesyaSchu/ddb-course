from django.shortcuts import render
from .models import *
# Create your views here.
from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponseNotFound
from datetime import date
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def postLoginUser(request):
    return render(request, 'post-login-user-index.html')


def postLoginAdmin(request):
    return render(request, 'post-login-admin-index.html')


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
        booking.place_id = Places.objects.only('place_id').filter(
            place_type_id=PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type")),
            available=True)[0]
        booking.save()

        last_place = Bookings.objects.values().latest("place_id")['place_id_id']
        place = Places.objects.get(place_id=last_place)
        place.available = False
        place.save(update_fields=["available"])
    else:
        booking = Bookings()
        guest = Guests()

    return render(request, 'add-booking.html', {
        'placetype': placetype
    })


def user_add_booking(request):
    placetype = PlaceType.objects.all()
    if request.method == 'POST':
        datee = request.POST.get("birthdate").split('/')
        b_date = date(int(datee[2]), int(datee[1]), int(datee[0]))
        print(datee, "####", b_date)
        guest = Guests(
            name=request.POST.get("name"),
            surname=request.POST.get("surname"),
            fathername=request.POST.get("fathername"),
            passport=request.POST.get("passport"),
            gender=request.POST.get("gender"),
            address=request.POST.get("address"),
            birthdate=b_date,
            phone_number=request.POST.get("phonenumber"),
            email=request.POST.get("booking-email"),
            )

        f = request.POST.get("arrival").split('/')
        l = request.POST.get("departure").split('/')
        f_date = date(int(f[2]), int(f[1]), int(f[0]))
        l_date = date(int(l[2]), int(l[1]), int(l[0]))
        delta = l_date - f_date
        price = PlaceType.objects.values().get(type=request.POST.get("room-type"))['PRICE']

        booking = Bookings(
            arrival_date=f_date,
            checkout_date=l_date,
            bk_id=BookingStatus.objects.only('bk_id').get(status="A"),
            guest_id=guest,
            money_total=price * delta.days,
            place_id=Places.objects.only('place_id').filter(
                place_type_id=PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type")), available=True)[0]
            )
        # place = Places(
        #     available=False,
        #     place_id=booking,
        #     place_type_id=PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type"))
        # )
     #   print("########", Places.objects.values().get(place_id=booking))
        s = Bookings.objects.values().get(place_id=booking)['place_id_id']
        place = Places.objects.get(place_id=s)
        place.available = False
        guest.save()
        booking.save()
        place.save(update_fields=["available"])
    else:
        booking = Bookings()
        guest = Guests()

    return render(request, 'user-add-booking.html', {
        'placetype': placetype
    })


def all_customer(request):
    customer_list = Guests.objects.all()
    return render(request, 'all-customer.html',
                  {
                      'customer_list': customer_list
                  }
                  )


def add_placetype(request):
    if request.method == "POST":
        try:
            last_ptype_ind = PlaceType.objects.values().latest("place_type_id")['place_type_id']
        except ObjectDoesNotExist:
            last_ptype_ind = 0
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


def user_all_placetype(request):
    ptype_list = PlaceType.objects.all()
    return render(request, 'user-placetype.html', {
        "ptype_list": ptype_list
    })


def all_services(request):
    service_list = Services.objects.all()
    return render(request, 'all-services.html', {
        "service_list": service_list
    })


def del_services(request, id):
    service_del_list = Services.objects.get(service_id=id)
    service_del_list.delete()
    service_list = Services.objects.all()

    return render(request, 'all-services.html', {
        'id': id,
        "service_list": service_list
    })


def user_all_services(request):
    service_list = Services.objects.all()
    return render(request, 'user-services.html', {
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


def del_placetype(request, id):
    ptype_del_list = PlaceType.objects.get(place_type_id=id)
    ptype_del_list.delete()
    ptype_list = PlaceType.objects.all()
    return render(request, 'all-placetype.html', {
        "ptype_list": ptype_list
    })


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


def user_all_room(request):
    places_list = Places.objects.all()
    ptypes = PlaceType.objects.all()
    return render(request, 'user-all-rooms.html',
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
        'placetype': placetype
    })


def all_booking(request):
    booking_list = Bookings.objects.all()
    print("ALL BOOKING:", booking_list)
    return render(request, 'all-booking.html',
                  {
                      'booking_list': booking_list
                  }
                  )


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
        booking.place_id = Places.objects.only('place_id').filter(
            place_type_id=PlaceType.objects.only('place_type_id').get(type=request.POST.get("room-type")),
            available=True)[0]
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
