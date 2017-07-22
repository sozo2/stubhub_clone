# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
import re
from django.core.urlresolvers import reverse


def index(request):
    if 'current_user_name' not in request.session:
        request.session['current_user_id'] = 0
    if 'action' not in request.session:
        request.session['action'] = ''
    return render(request, 'login_reg/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        request.session['action'] = 'register'
        if len(errors):
            for error, error_message in errors.iteritems():
                messages.error(request, error_message, extra_tags = error)
            return redirect('/')
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
            return redirect('/')
    else:
        return redirect('/')

# def authenticate(request):
#     if request.method == 'POST':
#         errors = User.objects.login_validator(request.POST)
#         request.session['action'] = 'login'
#         if len(errors):
#             for error, error_message in errors.iteritems():
#                 messages.error(request, error_message, extra_tags = error)
#             return redirect('/')
#         else:
#             email = request.POST['email']
#             this_user = User.objects.get(email = email)
#             this_user.save()
#             request.session['current_user_id'] = this_user.id
#             return redirect(REDIRECT TO INNER HOME PAGE) ********* needs editing
#     else:
#         return redirect('/')

# def load_home(request):
#     user = User.objects.get(id = request.session['current_user_id'])
#     context = {
#         'user' : user,
#     }
#     return render(request, 'log_reg/HOME HTML', context) ******* needs editing

def logout(request):
    request.session.clear()
    return redirect('/')
