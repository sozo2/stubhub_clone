# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request, listing_id):
    return render(request, 'checkout/index.html')


