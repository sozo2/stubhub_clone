# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import *
from django.utils import timezone
# Create your views here.

def index(request):
    user = User.objects.get(id = request.session['current_user_id'])
    listings = Listing.objects.filter(seller__id = request.session['current_user_id'])
    transactionSet=Transaction.objects.filter(buyer__id = request.session['current_user_id']).order_by('created_at')
    all_transactions = []
    for transaction in transactionSet:
        curr_dict = {}
        curr_dict['id']= transaction.id
        curr_dict['event']= transaction.listing.event.title
        curr_dict['start']= transaction.listing.event.start_time
        curr_dict['venue']= transaction.listing.event.venue.title
        curr_dict['city']= transaction.listing.event.venue.city
        curr_dict['section']= transaction.listing.section
        curr_dict['row']= transaction.listing.row
        curr_dict['tix']= transaction.tickets_bought
        curr_dict['future']= (transaction.listing.event.start_time > timezone.now())
        all_transactions.append(curr_dict)

    future_transactions= []    
    for transaction in transactionSet:
        if transaction.listing.event.start_time > timezone.now():
            curr_dict = {}
            curr_dict['id']= transaction.id
            curr_dict['event']= transaction.listing.event.title
            curr_dict['event_id']= transaction.listing.event.id
            curr_dict['start']= transaction.listing.event.start_time
            curr_dict['venue']= transaction.listing.event.venue.title
            curr_dict['city']= transaction.listing.event.venue.city
            curr_dict['section']= transaction.listing.section
            curr_dict['row']= transaction.listing.row
            curr_dict['tix']= transaction.tickets_bought
            curr_dict['future']= (transaction.listing.event.start_time > timezone.now())
            future_transactions.append(curr_dict)
                

    credit_cards = CreditCard.objects.filter(user__id = request.session['current_user_id'])
    display_name = user.first_name + " " + user.last_name[:1] +"."
    context = {
        "display_name" : display_name,
        "transactions" : all_transactions,
        "futuretrans": future_transactions
    }
    return render(request, "my_hub/index.html", context)

def gift_codes(request):
    return HttpResponse("This is the my_hub gift_codes page")

def favorites(request):
    return HttpResponse("This is the my_hub favorites")

def settings(request):
    return HttpResponse("This is the my_hub settings")