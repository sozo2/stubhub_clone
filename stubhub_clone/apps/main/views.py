# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse
from  models import *

def index(request):
    
    primaryPerformer = "Chicago Cubs"
    events = Event.objects.filter(performers__name=primaryPerformer)

    context = {
        'events':events,
        'primaryPerformer': primaryPerformer
    }
    return render(request, "main/index.html", context)