from apps.main.models import *


def createVenue(title,address,city,state,zip_code,seating_map):
    new_venue=Venue.objects.create(title=title,address=address,city=city,state=state,zip_code=zip_code,seating_map=seating_map)
    return new_venue

def printVenue(venue_id):
    if venue_id:
        venues = Venue.objects.filter(id = venue_id)
    else:
        venues=Venue.objects.all() 
    print '+' *50
    for venue in venues:
        print "Venue Title:", venue.title
        print "\tID:", venue.id
        print "\tAddress:", venue.address+',',venue.city+',',venue.state
        print "\tSeating Map:", venue.seating_map
        print '=' *50
    return venues.first()
            

def createPerformer(name,category,popularity,thumbnail):
    Performer.objects.create(name=name,category=category, popularity=popularity, thumbnail=thumbnail) 
    
def printPerformer(performer_id):
    if performer_id:
        performers = Performer.objects.filter(id = performer_id)
    else:
        performers=Performer.objects.all() 
    print '+' *50
    for performer in performers:
        print "Performer Name:", performer.name
        print "\tID:", performer.id
        print "\tCategory:", performer.category
        print "\tPopularity:", performer.popularity
        print "\tThumbnail:", performer.thumbnail
        print '=' *50
    return performers.first()
            

def createEvent(title,venue,performers,start_time,popularity,banner):
    Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#need to figure out how to handle multiple performers


def printEvent(event_id):
    if event_id:
        events = Event.objects.filter(id = event_id)
    else:
        events=Event.objects.all() 
    print '+' *50
    for event in events:
        print "Event title:", event.title
        print "\tID:", event.id
        print "\tVenue:", event.venue.title
        print "\tPerformers:",
        # for performer in performers:
        print performers.name
        print "\tStart Time:", event.start_time
        print "\tPopularity:", event.popularity
        print "\tBanner:", event.banner
        print '=' *50
    return events.first()

def createListing(seller,event,zone,section,tickets_for_sale,delivery_method):
    new_listing = Listing.objects.create(seller=seller,event=event,zone=zone,section=section,tickets_for_sale=tickets_for_sale, delivery_method=delivery_method)
    return new_listing.id

def printListing(listing_id):
    if listing_id:
        listings = Listing.objects.filter(id = listing_id)
    else:
        listings=Listing.objects.all() 
    print '+' *50
    for listing in listings:
        print "Listing Seller:", listing.seller.first_name,listing.seller.last_name
        print "\tID:\t", listing.id
        print "\tEvent:\t", listing.event.title 
        print "\tZone:", listing.zone
        print "\tSection:", listing.section
        print "\tTickets:", listing.tickets_for_sale
        print "\tDeliveryMethod:", listing.delivery_method
        print '=' *50
    return listings.first()


def printUser(user_id):
    if user_id:
        users = User.objects.filter(id = user_id)
    else:
        users=User.objects.all() 
    print '+' *50
    for user in users:
        print "User Name:", user.first_name,user.last_name
        print "\tID:\t", user.id
        print "\tEmail:\t", user.email 
        print "\tAddress:", user.address
        print "\t\t", user.city+', '+user.state+', '+user.zip_code
        print '=' *50
    return users.first()

def printTicket(ticket_id):
    if ticket_id:
        tickets = Ticket.objects.filter(id = ticket_id)
    else:
        tickets=Ticket.objects.all() 
    print '+' *50
    for ticket in tickets:
        print "ticket Seller:", ticket.listing.seller.first_name,ticket.listing.seller.last_name
        print "\tID:\t", ticket.id
        print "\tEvent:\t", ticket.listing.event.title 
        print "\tZone:", ticket.listing.zone
        print "\tSection:", ticket.listing.section
        print "\tSeat:", ticket.seat
        print "\tDeliveryPrices:", ticket.price
        print '=' *50
    return tickets.first()

def dbStats():
    venues_count = Venue.objects.count()
    print "Venues:",venues_count
    performers_count = Performer.objects.count()
    print "Performers:",performers_count
    events_count = Event.objects.count()
    print "Events:",events_count
    users_count = User.objects.count()
    print "Users:",users_count
    listings_count = Listing.objects.count()
    print "Listing:",listings_count
    tickets_count = Ticket.objects.count()
    print "Tickets:",tickets_count
