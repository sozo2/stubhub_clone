from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'gift_codes$', gift_codes),
    url(r'favorites$', favorites),
    url(r'settings$', settings),
   ]