from django.shortcuts import render
from .models import Bookings
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound


def index(request):
    return render(request, 'index.html')


def add_booking(request):
    return render(request, 'add-booking.html')


def create(request):
    if request.method == "POST":
        product = Bookings()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    # companies = Company.objects.all()
    # return render(request, "create.html", {"companies": companies})