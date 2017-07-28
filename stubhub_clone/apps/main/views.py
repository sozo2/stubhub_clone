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
from django.utils import timezone

def index(request):
    if 'user_status' not in request.session:
        request.session['user_status'] = 'logged out'
    if 'current_user_id' not in request.session:
        request.session['current_user_id'] = 0

    events = Event.objects.all().order_by('-popularity')[:1]
    performers_list = []
    events_list = Event.objects.all()
    print events_list
<<<<<<< HEAD
=======
    performers_list=[]
>>>>>>> fa44d8a4a012b735d354a7b52f97f017d208ebce
    for event in events_list:
        performers_list.append(event.performers.name)
    results=[]
    names = []
    for performer in performers_list:
        performerDict= {}
        existing = False
        for i in range(len(names)):
            if performer == names[i]:
                existing = True
        if existing:
            continue
        names.append(performer)
        performerDict['performer'] = performer
        performer_object = Performer.objects.get(name = performer)
        performerDict['thumbnail'] = performer_object.thumbnail
        performerEvents = Event.objects.filter(performers__name = performer,start_time__gte=timezone.now()).order_by('start_time')[:3]
        counter=1
        for event in performerEvents:
            curr_dict = {}
            curr_dict['day']=event.start_time
            curr_dict['time']=event.start_time
            curr_dict['title']=event.title
            curr_dict['venue']=event.venue.title
            curr_dict['date']=event.start_time
            curr_dict['id']=event.id
            performerDict['p'+str(counter)]=curr_dict
            counter+=1
        if counter >= 3:
            results.append(performerDict)
        if len(results) == 9:
            break      
    context = {
        'performers':results,
    }
    return render(request, "main/index.html", context)


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
    print '------------- logging OUT!@'
    request.session.clear()
    return redirect(reverse('main:index'))
