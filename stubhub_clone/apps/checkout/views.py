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
    request.session['total'] = total
    context = {
        'listing': listing,
        'total':total
    }
    return render(request, 'checkout/review.html', context)

def payment(request):
    return render(request, 'checkout/payment.html')

def confirmation(request):
    #creating creditcard object
    userID = request.session['current_user_id']
    userObject = User.objects.get(id=userID)
    nameOnCard = request.POST['cardOwner']
    cardNumber = request.POST['cardNumberOwner']
    expirationMonth = request.POST['expirationMonth']
    expirationYear = request.POST['expirationYear']
    expiration = str(expirationMonth+expirationYear)
    creditcardObject = CreditCard.objects.create(user=userObject, name_on_card=nameOnCard, number=cardNumber, expiration=expiration)

    #creating transaction object
    listingID = request.session['context']['listing']
    listingObject = Listing.objects.get(id=listingID)
    tickets = request.session['context']['tickets']
    total = request.session['total']
    Transaction.objects.create(buyer=userObject, listing=listingObject, tickets_bought=tickets, credit_card=creditcardObject, total=total)
    listingObject.tickets_for_sale = listingObject.tickets_for_sale - int(tickets)
    ticketSet = Ticket.objects.filter(listing__id = listingID).order_by('seat')
    if listingObject.tickets_for_sale == int(tickets):
        for ticket in ticketSet:
            ticket.sold = True
    # else:
    #     # for i in range(0, tickets):
    #     #     ticketSet[i].sold = True

    return redirect('/')
