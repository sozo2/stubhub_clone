# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Min
from django.utils import timezone
from datetime import *

# Create your views here.
def process(request):
    if request.method !="POST":
        return redirect(reverse('main:index')) 
    request.session['search_string'] = request.POST['searchInfo']
    return redirect(reverse ('search:results'))

def results(request):
    search_string = request.session['search_string']
    if len(Venue.objects.filter(title=search_string)):
        id = Venue.objects.get(title=search_string).id
        return redirect(reverse("search:venue",kwargs={'venue_id':id}))
    if len(Performer.objects.filter(name=search_string)):
        id = Performer.objects.get(name=search_string).id
        return redirect(reverse("search:performer",kwargs={'performer_id':id}))

    event_results = Event.objects.filter(title__icontains=search_string,start_time__gte=timezone.now()).order_by('start_time')
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
        curr_dict['min_price']= int(Ticket_Min['price__min'])
        
        events.append(curr_dict)
    
    context = {
        'search_results':events,
        'search_count':search_count
    }
    return render(request, 'find_tickets/results.html', context)
    
def event(request, event_id,sort_by='tickets__price'):
    try:
        if request.session['sort_by'] == sort_by:
            if request.session['asc'] == 1:
                request.session['asc'] = 0
                currsort='-'+sort_by
            else:
                request.session['asc'] = 1
                currsort=sort_by
        else:
            request.session['sort_by'] =sort_by
            currsort=request.session['sort_by']
            request.session['asc'] = 1
    except:
        request.session['sort_by'] =sort_by
        request.session['asc'] = 1
        currsort=request.session['sort_by']

    if 'sort_by' not in request.session:
        request.session['sort_by'] = sort_by
        
        
    event_all = Event.objects.get(id=event_id)
    event_dict={}
    event_dict['day']=event_all.start_time.strftime('%a')
    event_dict['time']=event_all.start_time.strftime('%I:%M %p')
    event_dict['title']=event_all.title
    event_dict['venue']=event_all.venue.title
    event_dict['date']=event_all.start_time.strftime('%b %d')
    event_dict['id']=event_all.id
    if event_all.venue.seating_map:
        event_dict['image']=event_all.venue.seating_map
    else:
        event_dict['image']="www.bykcollege.com/images/index/NoImageAvailable.png"
    print event_all.venue.seating_map

    if 'tix' not in request.session:
        desired_tickets= 1
    else:
        desired_tickets=request.session['tix']
    
    print currsort
    print request.session['asc']
    listings_all = Listing.objects.filter(event = event_all, tickets_for_sale__gte=desired_tickets).order_by(currsort).distinct()
    
    # for listing in listings_all:
    #    listing['best'] = int(listing['section']/100)/listing['row'] 
        

    listings = []
    for listing in listings_all:
        price = Ticket.objects.filter(listing=listing).first().price
        listing_dict={}
        listing_dict['zone'] = listing.zone
        listing_dict['section'] = listing.section
        listing_dict['row'] = listing.row
        listing_dict['price'] = '${:,.2f}'.format(price)
        listing_dict['num_tix'] = listing.tickets_for_sale
        listing_dict['delivery'] = listing.delivery_method
        listing_dict['id'] = listing.id
        listings.append(listing_dict)
    
    context = {
        'event':event_dict,
        'listings':listings,
    }
    
    return render(request,"find_tickets/event_home.html", context)
    
def ticket_change(request):
    if request.method != "POST":
        return redirect(reverse ('search:event'))        
    request.session['event_id'] = request.POST['event_id']
    try:
        request.session['tix'] = request.POST['numberOfTix']
    except:
        pass
    print request.session['tix'] , request.session['event_id']
    return redirect(reverse('search:event',kwargs={'event_id' : request.session['event_id']}))

def venue(request, venue_id):
    venue=Venue.objects.get(id = venue_id)
    event_results = Event.objects.filter(venue__id=venue_id,start_time__gte=timezone.now()).order_by('start_time')
    search_count = Event.objects.filter(venue__id=venue_id).count()
    
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
        curr_dict['min_price']= int(Ticket_Min['price__min'])
        
        events.append(curr_dict)
    
    context = {
        'search_results':events,
        'search_count':search_count,
        'venue_name':venue.title,
        'venue_banner':venue.banner,
    }
    return render(request, 'find_tickets/venue_home.html', context)
    
def performer(request, performer_id):
    performer = Performer.objects.get(id=performer_id) 
    event_results = Event.objects.filter(title__icontains=performer.name,start_time__gte=timezone.now()).order_by('start_time')
    search_count = Event.objects.filter(title__icontains=performer.name).count()
    
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
        curr_dict['min_price']= int(Ticket_Min['price__min'])
        
        events.append(curr_dict)
    
    context = {
        'search_results':events,
        'search_count':search_count,
        'performer_name':performer.name,
    }
    return render(request, 'find_tickets/performer_home.html', context)
    