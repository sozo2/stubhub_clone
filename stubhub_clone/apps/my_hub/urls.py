from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'gift_codes$', gift_codes,name='gift_codes'),
    url(r'favorites$', favorites,name='favorites'),
    url(r'settings$', settings,name='settings'),
    url(r'cc_delete/(?P<cc_id>\d+)$', cc_delete,name='cc_delete'),
    url(r'cc_add$', cc_add,name='cc_add'),
   ]