# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.core.urlresolvers import reverse
from django.db.models import Min
from datetime import *
import json

def index(request):
    if 'sell_search' not in request.session:
        request.session['sell_search'] = ""
    if 'listing_event_id' not in request.session:
        request.session['listing_event_id'] = 0
    if 'listing_id' not in request.session:
        request.session['listing_id'] = 0
    request.session['sell_stage'] = 'pending search'
    return render(request, 'sell_tickets/index.html')

def search(request):
    if request.method == "POST":
        request.session['sell_search'] = request.POST['search']
        return redirect(reverse ('sell:results'))
    else:
        return redirect(reverse ('sell:results'))

def results(request):
    search_string = request.session['sell_search']
    event_results = Event.objects.filter(title__icontains=search_string).order_by('start_time')
    search_count = Event.objects.filter(title__icontains=search_string).count()
    events=[]
    for search_result in event_results:
        curr_dict = {}
        Ticket_Min = Ticket.objects.filter(listing__event__id = search_result.id).aggregate(Min('price'))        
        curr_dict['day']=search_result.start_time.strftime('%a')
        curr_dict['time']=search_result.start_time.strftime('%-I:%M %p')
        curr_dict['title']= search_result.title
        curr_dict['venue']= search_result.venue.title
        curr_dict['date']=search_result.start_time.strftime('%b %d')
        curr_dict['id']=search_result.id
        curr_dict['avg_price']= search_result.average_price
        listing_count = Listing.objects.filter(event__id = search_result.id).count()
        curr_dict['listing_count'] = listing_count
        events.append(curr_dict)
    context = {
        'search_results':events,
        'search_count':search_count
    }
    request.session['sell_stage'] = 'return results'
    return render(request, 'sell_tickets/index.html', context)

def start_listing(request):
    request.session['listing_event_id'] = request.POST['event-selection']
    return redirect(reverse ('sell:info'))

def gather_info(request):
    event = Event.objects.get(id = request.session['listing_event_id'])
    event_title = event.title
    average_price = event.average_price
    if float(average_price) - 50 < 0:
        min_price = 0.00
    else:
        min_price = float(average_price) - 50 
    max_price = float(average_price) + 50.00
    context = {
        'title' : event_title,
        'price' : average_price,
        'price_min' : min_price,
        'price_max' : max_price,
        'event' : event 
    }
    return render(request, 'sell_tickets/info.html', context)

def create_listing(request):
    seller = User.objects.get(id = request.session['current_user_id'])
    event = Event.objects.get(id = request.session['listing_event_id'])
    if request.POST['GA'] == 'True':
        zone = 'GA'
        section = 'GA'
        row= 'GA'
    else:
        zone = request.POST['ticket-zone']
        section = request.POST['ticket-section']
        row = request.POST['ticket-row']
    tickets_for_sale = int(request.POST['ticket-number'])
    new_listing = Listing.objects.create(seller = seller, event = event, zone = zone, section = section, row = row, tickets_for_sale = tickets_for_sale)
    new_listing.save()
    request.session['listing_id'] = new_listing.id
    for i in range(tickets_for_sale):
        listing = new_listing
        price = request.POST['price-slider']
        if request.POST['GA'] == 'True':
            seat=0
        else:
            seat_string = request.POST['seat']
            seat_arr = seat_string.split(',')
            seat = seat_arr[i]
        new_ticket = Ticket.objects.create(listing = listing, price = price, seat = seat)
        new_ticket.save()
    return redirect(reverse ('sell:landing'))

def load_landing_page(request):
    return redirect(reverse ('main:index'))


