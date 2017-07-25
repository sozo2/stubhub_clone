# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import *

# Create your views here.
def process(request):
    if request.method !="POST":
        return redirect(reverse('main:index')) 
    request.session['search_string'] = request.POST['searchInfo']
    return redirect(reverse ('search:results'))

def results(request):
    search_string = request.session['search_string']
    search_results = Event.objects.filter(title__icontains=search_string).order_by('start_time')
    search_count = Event.objects.filter(title__icontains=search_string).count()
    results=[]
    for search_result in search_results:
        curr_dict = {}
        curr_dict['day']=search_result.start_time.strftime('%a')
        curr_dict['time']=search_result.start_time.strftime('%I:%M %p')
        curr_dict['title']= search_result.title
        curr_dict['venue']= search_result.venue.title
        curr_dict['date']=search_result.start_time.strftime('%b %d')
        results.append(curr_dict)
    context = {
        'search_results':results,
        'search_count':search_count
    }
    return render(request, 'find_tickets/results.html', context)
    
def event(request, event_id):
    return render(request,"find_tickets/event_home.html")
    