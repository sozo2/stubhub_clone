# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse
from  models import *

def index(request):
    events = Event.objects.all().order_by('-popularity')[:1]
    # for event in events:
    #     performers = event.performers.all()
    #     for i in range(len(performers)):
    #         if i == 0:
    #             print performers[i].name
    context = {
        'events':events,
    }
    return render(request, "main/index.html", context)