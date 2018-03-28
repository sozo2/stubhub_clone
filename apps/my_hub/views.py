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
    user_dict = {}
    user_dict['first']=user.first_name
    user_dict['last']=user.last_name
    user_dict['email']=user.email
    user_dict['address']=user.address
    user_dict['city']=user.city
    user_dict['state']=user.state
    user_dict['zip']=user.zip_code


    listingSet = Listing.objects.filter(seller__id = request.session['current_user_id']).order_by('created_at')
    all_listings = []
    for listing in listingSet:
        curr_dict = {}
        curr_dict['id']= listing.id
        curr_dict['event']= listing.event.title
        curr_dict['event_id']= listing.event.id
        curr_dict['start']= listing.event.start_time
        curr_dict['venue']= listing.event.venue.title
        curr_dict['venue_id']= listing.event.venue.id
        curr_dict['city']= listing.event.venue.city
        curr_dict['section']= listing.section
        curr_dict['row']= listing.row
        curr_dict['tix']= listing.tickets_for_sale
        curr_dict['future']= (listing.event.start_time > timezone.now())
        all_listings.append(curr_dict)
    active_listings= []    
    for listing in listingSet:
        if listing.event.start_time > timezone.now() and listing.tickets_for_sale:
            curr_dict = {}
            curr_dict['id']= listing.id
            curr_dict['event']= listing.event.title
            curr_dict['event_id']= listing.event.id
            curr_dict['start']= listing.event.start_time
            curr_dict['venue']= listing.event.venue.title
            curr_dict['venue_id']= listing.event.venue.id
            curr_dict['city']= listing.event.venue.city
            curr_dict['section']= listing.section
            curr_dict['row']= listing.row
            curr_dict['tix']= listing.tickets_for_sale
            curr_dict['future']= (listing.event.start_time > timezone.now())
            active_listings.append(curr_dict)

    transactionSet=Transaction.objects.filter(buyer__id = request.session['current_user_id']).order_by('created_at')
    all_transactions = []
    for transaction in transactionSet:
        curr_dict = {}
        curr_dict['id']= transaction.id
        curr_dict['event']= transaction.listing.event.title
        curr_dict['event_id']=transaction.listing.event.id
        curr_dict['start']= transaction.listing.event.start_time
        curr_dict['venue']= transaction.listing.event.venue.title
        curr_dict['venue_id']= transaction.listing.event.venue.id
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
            curr_dict['venue_id']= transaction.listing.event.venue.id
            curr_dict['city']= transaction.listing.event.venue.city
            curr_dict['section']= transaction.listing.section
            curr_dict['row']= transaction.listing.row
            curr_dict['tix']= transaction.tickets_bought
            curr_dict['future']= (transaction.listing.event.start_time > timezone.now())
            future_transactions.append(curr_dict)
                
    salesSet=Transaction.objects.filter(listing__seller__id = request.session['current_user_id']).order_by('created_at')
    all_sales = []
    for sales in salesSet:
        curr_dict = {}
        curr_dict['id']= sales.id
        curr_dict['event']= sales.listing.event.title
        curr_dict['event_id']=sales.listing.event.id
        curr_dict['start']= sales.listing.event.start_time
        curr_dict['venue']= sales.listing.event.venue.title
        curr_dict['venue_id']= sales.listing.event.venue.id
        curr_dict['city']= sales.listing.event.venue.city
        curr_dict['section']= sales.listing.section
        curr_dict['row']= sales.listing.row
        curr_dict['tix']= sales.tickets_bought
        curr_dict['future']= (sales.listing.event.start_time > timezone.now())
        all_sales.append(curr_dict)

    credit_cards = CreditCard.objects.filter(user__id = request.session['current_user_id'])

    all_ccs = []
    for cc in credit_cards:
        curr_dict = {}
        curr_dict['num_end']= cc.number[-4:]
        first_two_dig = cc.number[:2]
        if first_two_dig == 34 or first_two_dig == 37:
            curr_dict['thumbnail']= 'upload.wikimedia.org/wikipedia/commons/thumb/3/30/American_Express_logo.svg/2000px-American_Express_logo.svg.png'
        elif first_two_dig>=50 and first_two_dig <56:
            curr_dict['thumbnail']='upload.wikimedia.org/wikipedia/commons/thumb/b/b7/MasterCard_Logo.svg/2000px-MasterCard_Logo.svg.png'
        else:
            curr_dict['thumbnail']='upload.wikimedia.org/wikipedia/commons/6/6a/Visa-europe-logo.gif'
        
        curr_dict['name']= cc.name_on_card 
        curr_dict['exp_date']=cc.expiration[:2]+'/'+cc.expiration[2:]
        curr_dict['id']=cc.id
        all_ccs.append(curr_dict)

    
    display_name = user.first_name + " " + user.last_name[:1] +"."
    
    context = {
        "display_name" : display_name,
        "transactions" : all_transactions,
        "futuretrans": future_transactions,
        "listings" : all_listings,
        "activelists": active_listings,
        "all_sales": all_sales,
        "user": user_dict,
        "ccs": all_ccs
     }
    return render(request, "my_hub/index.html", context)

def gift_codes(request):
    return HttpResponse("This is the my_hub gift_codes page")

def favorites(request):
    return HttpResponse("This is the my_hub favorites")

def settings(request):
    return HttpResponse("This is the my_hub settings")

def cc_delete(request,cc_id):
    CreditCard.objects.get(id=cc_id).delete()
    return redirect(reverse('my_hub:index'))

def cc_add_form(request):
    return render(request, "my_hub/add_cc_form.html")

def cc_add(request):
    if request.method != "POST":
        return redirect(reverse('my_hub:index'))
    number = request.POST['card_number']
    name_on_card =request.POST['name_on_card']
    exp_date=request.POST['expirationMonth']+request.POST['expirationYear']    

    print CreditCard.objects.create(user_id = request.session['current_user_id'],number =number, name_on_card=name_on_card,expiration=exp_date)    
    return redirect(reverse('my_hub:index'))