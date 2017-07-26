from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^/(?P<listing_id>\d+)$', index, name="index"),
    url(r'^process/(?P<listing_id>\d+)$', process, name='process'),
    url(r'/review$', review, name='review'),
    url(r'/payment$', payment, name='payment'),
]