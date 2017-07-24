# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def results(request):
    if request.method !="POST":
        return redirect(reverse('main:index')) 
    #search_query = request.POST['query']
    search_events=Event.objects.filter(string_icontains="")
