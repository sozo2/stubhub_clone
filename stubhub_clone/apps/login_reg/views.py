# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse

def login_reg(request):
    return HttpResponse("Login or Register")

def authenticate(request):
    return HttpResponse("Authenticate")

def register(request):
    return HttpResponse("Register")

# Create your views here.
