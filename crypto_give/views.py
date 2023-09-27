from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .models import Transactions, Slot

# Create your views here.

def handler404(requests, exception):
    return HttpResponseRedirect('/')

def home(requests):
    transaction= Transactions.objects.all()
    slots= Slot.objects.all()
    return render(requests, "home.html", {"slots":slots, "transaction":transaction})