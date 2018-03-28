from __future__ import unicode_literals
import django
from django.shortcuts import render, redirect, HttpResponse
from django.db import models
from apps.main.models import *
from datetime import datetime
import requests
import json


from apps.main.models import *
import csv
import random

# import importStubhub


def build_users():
###############################################
# #BUILD USERS
    with open("user_file.csv",'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    for x in your_list:
        print "*************"
        first_name = x[0]
        # print first_name, 
        last_name = x[1]
        # print last_name
        email = x[2]
        print email
        password = "12345"
        # print password
        address = x[3]
        # print address 
        city = x[4]
        # print city
        state = x[5]
        # print state
        zip_code = x[6]
        # print zip_code
        
        User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,address=address,city=city,state=state,zip_code=zip_code)



def get_chicago_seatgeek():
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
                try:    
                    thumbnail = event_list[i]['performers'][0]['image']
                except:
                    thumbnail = None
                new_performer = Performer.objects.create(name = name, category = category, thumbnail = thumbnail)
                new_performer.save()
                print "Performer %s was created" % new_performer.name 
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
                print "\t Venue %s was created" % new_venue.title
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
            start_time = datetime.strptime(time_string, '%Y-%m-%dT%X')
            popularity = event_popularity
            average_price = event_list[i]['stats']['lowest_price_good_deals']
            if not average_price:
                average_price = 55.00
            new_event = Event.objects.create(title = event_title, venue = venue, performers = performers, start_time = start_time, popularity = popularity, average_price = average_price)
            new_event.save()
            print "\t\t Event %s was created" % new_event.title

def create_listings():
#############################################
# # #CREATING LISTINGS 
# # X listings for every event each time this block runs
    listings = 10
    all_events = Event.objects.all()

    delivery_method = "Print From Home"
    for event in all_events:
        for i in range(0,listings):
            seller = User.objects.get(id = random.randint(1,5))
            zone = random.randint(1,9)
            section = random.randint(101,301)
            tickets_for_sale = random.randint(1,12)
            delbool = random.randint(1,2)
            if delbool == 1: 
                delivery_method = "Electronic"
            else:   
                delivery_method = "Mail"
            createListing(seller,event,zone,section,tickets_for_sale,delivery_method)


def create_tickets():
############################################
##CREATE Ticket record for each ticket in each listing

    all_listings = Listing.objects.all()
    for listing in all_listings:
        seat = random.randint(1,5)
        price = random.randint(50, 200)
        for x in range(0,listing.tickets_for_sale):
            this_ticket=Ticket.objects.create(listing=listing, seat=seat,price=price)
            seat+=1
            print this_ticket.id

def add_venue_thumbs():
    venues = {
            'United Center' : 'www.unitedcenter.com/assets/1/7/chicago_bulls_seating_chart.gif',
            'Wrigley Field' : 'chicago.cubs.mlb.com/chc/images/ticketing/sth/y2016/2018-Wrigley-Field-Seating-Map-3D-large.jpg',
            'Guaranteed Rate Field': 'maps.seatics.com/UsCellularField_Baseball_2009-05-01_2011-07-29_0940_tn.gif',
            'CIBC Theatre': 'www.theatreinchicago.com/images/seat/cibc-theatre-seating-chart.jpg',
    }

    for key, value in venues.iteritems():
        event_venue = Venue.objects.filter(title = key)
        for venue in event_venue:
            venue.seating_map = value
            venue.save()

build_users()
get_chicago_seatgeek()
add_venue_thumbs()
create_listings()
create_tickets()