from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
import re
from django.core.urlresolvers import reverse
from django.core import serializers
import json
from django.http import JsonResponse

def index(request):
    #context = {
     #   'events':events,
    #}
    return render(request, "main/index.html")


def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        request.session['action'] = 'register'
        if len(errors):
            msgs =[]
            fail = True
            for error, error_message in errors.iteritems():
                msgs.append(error_message)
            context = {"messages" : msgs, "fail" : fail}
            return JsonResponse(context)
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            secret_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = secret_password)
            new_user.save()
            request.session['current_user_id'] = new_user.id
            request.session['action'] = 'register success'
            request.session['user_status'] = 'logged in'
            context = {"fail" : False}
            return JsonResponse(context)
    else:
        return JsonResponse({"RESPONSE": 12123})

def authenticate(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        request.session['action'] = 'login'
        if len(errors):
            msgs =[]
            fail = True
            for error, error_message in errors.iteritems():
                msgs.append(error_message)
            context = {"messages" : msgs, "fail" : fail}
            return JsonResponse(context)
        else:
            email = request.POST['email']
            this_user = User.objects.get(email = email)
            this_user.save()
            request.session['current_user_id'] = this_user.id
            request.session['user_status'] = 'logged in'
            context = {"fail" : False}
            return JsonResponse(context)
    else:
        return JsonResponse({"RESPONSE": 12123})

def logout(request):
    request.session.clear()
    return redirect(reverse('main:index'))
