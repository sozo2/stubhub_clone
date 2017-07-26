from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^/(?P<listing_id>\d+)$', index, name="index"),
]