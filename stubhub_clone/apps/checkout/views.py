# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.db.models import Min

def index(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    minSeat = Ticket.objects.filter(listing=listing_id).aggregate(Min('seat'))
    seatPrice = Ticket.objects.filter(listing=listing_id).aggregate(Min('price'))
    minSeats =  minSeat['seat__min']
    price = seatPrice['price__min']
    maxSeats = minSeats+listing.tickets_for_sale
    context = {
        'listing': listing,
        'minSeat':minSeats,
        'maxSeat':maxSeats,
        'price':price
    }
    return render(request, 'checkout/index.html', context)

def review(request):
    return render(request, 'checkout/review.html')

