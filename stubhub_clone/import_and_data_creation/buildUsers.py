from apps.main.models import *
import csv
import random
import datetime

###############################################
#BUILD USERS
with open("user_file.csv",'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

for x in your_list:
    print "*************"
    first_name = x[0]
    print first_name, 
    last_name = x[1]
    print last_name
    email = x[2]
    print email
    password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    print password
    address = x[3]
    print address 
    city = x[4]
    print city
    state = x[5]
    print state
    zip_code = x[6]
    print zip_code
    User.objects.create(first_name=first_name,last_name=last_name,email=email,password=password,address=address,city=city,state=state,zip_code=zip_code)
