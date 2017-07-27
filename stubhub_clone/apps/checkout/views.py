# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.db.models import Min
from django.urls import reverse

def index(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    minSeat = Ticket.objects.filter(listing=listing_id).aggregate(Min('seat'))
    seatPrice = Ticket.objects.filter(listing=listing_id).aggregate(Min('price'))
    minSeats =  minSeat['seat__min']
    price = seatPrice['price__min']
    maxSeats = minSeats+listing.tickets_for_sale
    maxSeatsList = []
    for item in range(0, listing.tickets_for_sale):
        maxSeatsList.append(item + 2)

    context = {
        'listing': listing,
        'minSeat':minSeats,
        'maxSeat':maxSeats,
        'maxSeatsList': maxSeatsList,
        'price':price,
    }
    return render(request, 'checkout/index.html', context)

def process(request, listing_id):
    tickets = request.POST['numberOfTix']
    priceOfTix = request.POST['priceOfTix']
    listing = Listing.objects.get(id=listing_id)
    minSeat = Ticket.objects.filter(listing=listing_id).aggregate(Min('seat'))
    seatPrice = Ticket.objects.filter(listing=listing_id).aggregate(Min('price'))
    minSeats =  minSeat['seat__min']
    price = seatPrice['price__min']
    maxSeats = minSeats+listing.tickets_for_sale
    request.session['context'] = {
        'listing': listing.id,
        'minSeat':minSeats,
        'maxSeat':maxSeats,
        'price':price,
        'tickets':tickets,
        'priceOfTix':priceOfTix
    }
    return redirect(reverse('checkout:review'))

def review(request):
    listingID = request.session['context']['listing']
    listing = Listing.objects.get(id=listingID)
    tickets =request.session['context']['tickets']
    ticketPrice = request.session['context']['price']
    total = float(tickets)*ticketPrice
    context = {
        'listing': listing,
        'total':total
    }
    return render(request, 'checkout/review.html', context)

def payment(request):
    return render(request, 'checkout/payment.html')

def confirmation(request):
    print request.session['current_user_id']
    nameOnCard = request.POST['owner']
    cardNumber = request.POST['cardNumber']
    expirationMonth = request.POST['expirationMonth']
    expirationYear = request.POST['expirationYear']
    return redirect('/')
