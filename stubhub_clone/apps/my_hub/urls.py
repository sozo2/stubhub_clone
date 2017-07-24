from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'gift_codes$', gift_codes,name='gift_codes'),
    url(r'favorites$', favorites,name='favorites'),
    url(r'settings$', settings,name='settings'),
   ]