# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    return HttpResponse("This is the my_hub home")

def gift_codes(request):
    return HttpResponse("This is the my_hub gift_codes page")

def favorites(request):
    return HttpResponse("This is the my_hub favorites")

def settings(request):
    return HttpResponse("This is the my_hub settings")