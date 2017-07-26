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
    return render(request, 'sell_tickets/index.html')

def search(request):
    if request.method == "POST":
        request.session['sell_search'] = request.POST['search']
        print request.session['sell_search']
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
        curr_dict['time']=search_result.start_time.strftime('%I:%M %p')
        curr_dict['title']= search_result.title
        curr_dict['venue']= search_result.venue.title
        curr_dict['date']=search_result.start_time.strftime('%b %d')
        curr_dict['id']=search_result.id
        curr_dict['avg_price']= search_result.average_price
        events.append(curr_dict)
    context = {
        'search_results':events,
        'search_count':search_count
    }
    return render(request, 'sell_tickets/index.html', context)

def start_listing(request):
    request.session['listing_event_id'] = request.POST['event-selection']
    return redirect(reverse ('sell:info'))

def gather_info(request):
    event = Event.objects.get(id = request.session['listing_event_id'])
    event_title = event.title
    average_price = event.average_price
    context = {
        'title' : event_title,
        'price' : average_price
    }
    return render(request, 'sell_tickets/info.html', context)