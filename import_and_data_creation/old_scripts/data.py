from __future__ import unicode_literals
import django
from django.shortcuts import render, redirect, HttpResponse
from django.db import models
from apps.main.models import *
from datetime import *
import requests
import json

def grab_data():
    response = requests.get("https://api.seatgeek.com/2/events?venue.city=Chicago&client_id=ODI3OTE5M3wxNTAxMDIxODIzLjUy&per_page=3000")
    my_events = response.json()
    event_list = my_events['events']
    for i in range(len(event_list)):
        #performer creation
        event_popularity = event_list[i]['score']
        if event_popularity > 0.5:
            new_performer_name = event_list[i]['performers'][0]['name']
            existing_performers = Performer.objects.filter(name = new_performer_name)
            if len(existing_performers) == 0:
                name = new_performer_name
                category = event_list[i]['performers'][0]['type']
                thumbnail = event_list[i]['performers'][0]['image']
                new_performer = Performer.objects.create(name = name, category = category, thumbnail = thumbnail)
                new_performer.save()
                event_performer = new_performer
            else:
                event_performer = Performer.objects.get(name = new_performer_name)
            new_venue_name = event_list[i]['venue']['name']
            existing_venues = Venue.objects.filter(title = new_venue_name)
            if len(existing_venues) == 0:
                title = new_venue_name
                address = event_list[i]['venue']['address']
                city = event_list[i]['venue']['city']
                state = event_list[i]['venue']['state']
                zip_code = event_list[i]['venue']['postal_code']
                new_venue = Venue.objects.create(title = title, address = address, city = city, state = state, zip_code = zip_code)
                new_venue.save()
                event_venue = new_venue
            else:
                event_venue = Venue.objects.get(title = new_venue_name)

            try:
                event_title = event_list[i]['short_title']
            except:
                event_title = event_list[i]['title']
            
            if event_title.endswith(' - Chicago'):
                event_title= event_title[:-10]
            venue = event_venue
            performers = event_performer
            time_string = event_list[i]['datetime_local']
            start_time = datetime(year=int(time_string[0:4]), month=int(time_string[5:7]), day=int(time_string[8:10]), hour=int(time_string[11:13]), minute=int(time_string[14:16]))
            popularity = event_popularity
            average_price = event_list[i]['stats']['lowest_price_good_deals']
            if not average_price:
                average_price = 55.00
            new_event = Event.objects.create(title = event_title, venue = venue, performers = performers, start_time = start_time, popularity = popularity, average_price = average_price)
            new_event.save()
    return

grab_data()