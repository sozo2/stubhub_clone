# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse
from  models import *

def index(request):
    events = Event.objects.all().order_by('-popularity')[:1]
    performers_list = ["Chicago Cubs", "Chicago White Sox", "Houston Astros", "New York Yankees", "Washington Nationals", "Los Angeles Dodgers",]
    results=[]
    for performer in performers_list:
        performerDict= {}
        performerDict['performer'] = performer
        performerEvents = Event.objects.filter(performers__name = performer).order_by('start_time')[:3]
        counter=1
        for event in performerEvents:
            curr_dict = {}
            curr_dict['day']=event.start_time
            curr_dict['time']=event.start_time
            curr_dict['title']=event.title
            curr_dict['venue']=event.venue.title
            curr_dict['date']=event.start_time
            performerDict['p'+str(counter)]=curr_dict
            counter+=1
        results.append(performerDict)
    print results
    for performer in results:
        print performer['p1']
        print performer['p2']
    context = {
        'performers':results,
    }
    return render(request, "main/index.html", context)