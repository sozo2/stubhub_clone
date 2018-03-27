from apps.main.models import *
import random
#from importGrubhub import *

#############################################
##CREATING LISTINGS 
#20 listings for each event each time this block runs

all_events = Event.objects.all()

delivery_method = "Print From Home"
count = 1
for event in all_events:
    for i in range(0,random.randint(1,10)):
        seller = User.objects.get(id = random.randint(1,10))
        zone = random.randint(1,9)
        section = random.randint(101,301)
        tickets_for_sale = random.randint(1,12)
        delbool = random.randint(1,2)
        if delbool == 1: 
            delivery_method = "Electronic"
        else:   
            delivery_method = "Mail"
        x = createListing(seller,event,zone,section,tickets_for_sale,delivery_method)
        listing = Listing.objects.get(id = x)
        print "Created listing ", count
        count+=1
        seat = random.randint(1,5)
        price = random.randint(50, 200)
        for x in range(0,listing.tickets_for_sale):
            this_ticket=Ticket.objects.create(listing=listing, seat=seat,price=price)
            seat+=1
            print "\tCreated Ticket", this_ticket.id

############################################
##CREATE Ticket record for each ticket in each listing
# #
# all_listings = Listing.objects.all()
# for listing in all_listings:
#     seat = random.randint(1,5)
#     price = random.randint(50, 200)
#     for x in range(0,listing.tickets_for_sale):
#         this_ticket=Ticket.objects.create(listing=listing, seat=seat,price=price)
#         seat+=1
#         print this_ticket.id
        

        
