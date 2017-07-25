# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse
import bcrypt
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    def register_validator(self, user_input):
        errors = {}
        input_email = user_input['email']
        check_email_list = User.objects.filter(email = input_email)
        if len(check_email_list) <> 0:
            errors['existing'] = 'This email is already registered. Log in.'
        if len(user_input['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 characters long'
        if not (user_input['first_name']).isalpha() or not (user_input['last_name']).isalpha():
            errors['name_chars'] = 'Name fields can only contain letters of the alphabet'
        if len(user_input['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters long'
        if len(user_input['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if not EMAIL_REGEX.match(user_input['email']):
            errors['email'] = 'Email syntax not valid.'
        return errors 
    def login_validator(self, user_input):
        errors = {}
        input_email = user_input['email']
        input_password = user_input['password']
        check_user = User.objects.filter(email = input_email)
        if len(check_user) == 0:
            errors['not_registered'] = 'Email not in system. Register first before attempting login.'
        if not bcrypt.checkpw(input_password.encode(), check_user[0].password.encode()):
            errors['wrong_password'] = 'Incorrect password. Please try again.'
        return errors 

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 45)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 45)
    state = models.CharField(max_length = 45)
    zip_code = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
  
class Performer(models.Model):
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    popularity = models.IntegerField(default = 0)
    thumbnail = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 

class Venue(models.Model):
    title = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 45)
    state = models.CharField(max_length = 45)
    zip_code = models.CharField(max_length = 45)
    seating_map = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)      

class Event(models.Model):
    title = models.CharField(max_length = 255)
    venue = models.ForeignKey(Venue, related_name = 'events')
    performers = models.ManyToManyField(Performer, related_name = 'events')
    start_time = models.DateTimeField(default=datetime.now)
    popularity = models.IntegerField(default = 0)
    banner = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  

class Listing(models.Model):
    seller = models.ForeignKey(User, related_name = 'listings')
    event = models.ForeignKey(Event,related_name = 'listings')
    zone = models.CharField(max_length = 255)
    section = models.CharField(max_length = 255)
    row = models.CharField(max_length=45,default = 'A')
    tickets_for_sale = models.IntegerField(default = 0)
    delivery_method = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 

class Ticket(models.Model):
    listing = models.ForeignKey(Listing, related_name = 'tickets')
    seat = models.IntegerField(default = 0)
    price = models.FloatField(default = 0.0)
    sold = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  

class CreditCard(models.Model):
    user = models.ForeignKey(User, related_name = 'credit_cards')
    name_on_card = models.CharField(max_length = 255)
    number = models.CharField(max_length = 45)
    expiration = models.CharField(max_length = 16)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 

class Transaction(models.Model):
    buyer = models.ForeignKey(User, related_name = 'transactions') 
    listing = models.ForeignKey(Listing, related_name = 'transactions')
    tickets_bought = models.IntegerField(default = 0)
    credit_card = models.ForeignKey(CreditCard, related_name = 'transactions')
    total = models.FloatField(default = 0.0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 


