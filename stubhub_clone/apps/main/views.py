# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse

def index(request):
    return HttpResponse("StubHUb Home")

# Create your views here.
