from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
   # url(r'^/authenticate$', authenticate),
    url(r'register$', register),
    url(r'logout$', logout)
]