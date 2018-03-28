# ##########################################333
# # #BUILD EVENTS FOR MUSIC 
# #
# def makeList(low, high):
#     counter = low
#     list = []
#     while counter <= high:
#         list.append(counter)
#         counter +=1
#     return list

# performerList = makeList(19,32)
# print performerList 
# venueList = makeList(1,12) 
# print venueList

# for performer_id in performerList:
#     for i in range(1,random.randint(2,4)):
#         venue_id = random.randint(1,12)
#         start_time = datetime.datetime.now() + datetime.timedelta(days=random.randint(1,90))
#         performers = Performer.objects.get(id = performer_id)
#         performers.save()
#         venue = Venue.objects.get(id = venue_id)
#         title = performers.name+" at "+venue.title
#         popularity = performers.popularity*1000
#         banner="Location of event banner"
#         print title,venue,performers,start_time,popularity,banner
#         new_event = Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#         new_event.save()
#         new_event.performers.add(performers)
    
    
# # # Build Sox Games
# start_time = datetime.datetime.now() 
# performer1 = Performer.objects.get(id = 1)
# performer1.save()
# venue = Venue.objects.get(id = 7)        
# games=0
# banner="Location of event banner"        
# while (games<15):    
#     performer2 = Performer.objects.get(id = random.randint(3,7))
#     performer2.save()
#     title = performer2.name+" at "+performer1.name
#     popularity = (performer1.popularity+performer2.popularity)*500    
#     series=0
#     while series<4:
#         print title,venue,performers,start_time,popularity,banner
#         new_event = Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#         new_event.save()
#         new_event.performers.add(performer1)
#         new_event.performers.add(performer2)
#         series+=1
#         games+=1
#         start_time=start_time+datetime.timedelta(days=1)
#     start_time=start_time+datetime.timedelta(days=random.randint(1,2))
    
# # # Build Cubs Games
# start_time = datetime.datetime.now() 
# performer1 = Performer.objects.get(id = 2)
# performer1.save()
# venue = Venue.objects.get(id = 3)        
# games=0
# banner="Location of event banner"        
# while (games<30):    
#     performer2 = Performer.objects.get(id = random.randint(3,7))
#     performer2.save()
#     title = performer2.name+" at "+performer1.name
#     popularity = (performer1.popularity+performer2.popularity)*500    
#     series=0
#     while series<4:
#         print title,venue,performers,start_time,popularity,banner
#         new_event = Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#         new_event.save()
#         new_event.performers.add(performer1)
#         new_event.performers.add(performer2)
#         series+=1
#         games+=1
#         start_time=start_time+datetime.timedelta(days=1)
#     start_time=start_time+datetime.timedelta(days=random.randint(1,2))

# # # Build Hawks Games
# start_time = datetime.datetime.now() 
# performer1 = Performer.objects.get(id = 16)
# performer1.save()
# venue = Venue.objects.get(id = 2)        
# games=0
# banner="Location of event banner"        
# while (games<15):    
#     performer2 = Performer.objects.get(id = random.randint(17,18))
#     performer2.save()
#     title = performer2.name+" at "+performer1.name
#     popularity = (performer1.popularity+performer2.popularity)*500    
#     print title,venue,performers,start_time,popularity,banner
#     new_event = Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#     new_event.save()
#     new_event.performers.add(performer1)
#     new_event.performers.add(performer2)
#     games+=1
#     start_time=start_time+datetime.timedelta(days=random.randint(1,7))

# # #Build Bulls Games
# start_time = datetime.datetime.now() 
# performer1 = Performer.objects.get(id = 9)
# performer1.save()
# venue = Venue.objects.get(id = 2)        
# games=0
# banner="Location of event banner"        
# while (games<15):    
#     performer2 = Performer.objects.get(id = random.randint(10,12))
#     performer2.save()
#     title = performer2.name+" at "+performer1.name
#     popularity = (performer1.popularity+performer2.popularity)*500    
#     print title,venue,performers,start_time,popularity,banner
#     new_event = Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#     new_event.save()
#     new_event.performers.add(performer1)
#     new_event.performers.add(performer2)
#     games+=1
#     start_time=start_time+datetime.timedelta(days=random.randint(1,7))

# # #Build Bears Games
# ##
# start_time = datetime.datetime.now()+datetime.timedelta(days=6) 
# performer1 = Performer.objects.get(id = 13)
# performer1.save()
# venue = Venue.objects.get(id = 1)        
# games=0
# banner="Location of event banner"        
# while (games<15):    
#     performer2 = Performer.objects.get(id = random.randint(14,15))
#     performer2.save()
#     title = performer2.name+" at "+performer1.name
#     popularity = (performer1.popularity+performer2.popularity)*500    
#     print title,venue,performers,start_time,popularity,banner
#     new_event = Event.objects.create(title=title,venue=venue,start_time=start_time,popularity=popularity, banner=banner)
#     new_event.save()
#     new_event.performers.add(performer1)
#     new_event.performers.add(performer2)
#     games+=1
#     start_time=start_time+datetime.timedelta(days=7)

#BUILD VENUES
# createVenue('Soldier Field', '1410 Museum Campus Dr', 'Chicago', 'IL', '60610','location of staticfile')
# createVenue('United Center', '1901 W Madison St', 'Chicago', 'IL', '60612','location of staticfile')
# createVenue('Wrigley Field', '1060 W. Addison St.', 'Chicago', 'IL', '60613','location of staticfile')
# createVenue('The Empty Bottle', '1035 N. Western Ave', 'Chicago', 'IL', '60612','location of staticfile')
# createVenue('Subterranean', '2011 W North Ave', 'Chicago', 'IL', '60612','location of staticfile')
# createVenue('Bottom Lounge', '1375 W. Lake Street', 'Chicago', 'IL', '60613','location of staticfile')
# createVenue('Guaranteed Rate Loan Park', '1410 Museum Campus Dr', 'Chicago', 'IL', '60610','location of staticfile')
# createVenue('The Hideout', ' 1354 W Wabansia Ave', 'Chicago', 'IL', '60642','location of staticfile')
# createVenue('Thalia Hall', '1807 S Allport St', 'Chicago', 'IL', '60608','location of staticfile')
# createVenue('Lincoln Hall', '2424 N Lincoln Ave', 'Chicago', 'IL', '60614','location of staticfile')
# createVenue('Schubas Tavern', '3159 N Southport Ave', 'Chicago', 'IL', '60657','location of staticfile')
# createVenue('Kingston Mines', '2548 N Halsted St', 'Chicago', 'IL', '60614','location of staticfile')
# # for above, run after executing ImportGrubhub.py
# ################################################
# #BUILD PERFORMERS

# with open("performer_file.csv",'rb') as f:
#     reader = csv.reader(f)
#     your_list = list(reader)

# for x in your_list:
#     name = x[0]
#     print name, 
#     category = x[1]
#     print category,
#     popularity = x[2]
#     print popularity,
#     thumbnail = x[3]
#     print thumbnail
#     Performer.objects.create(name=name,category=category,popularity=popularity,thumbnail=thumbnail)