from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^authenticate$', authenticate, name='login'),
    url(r'register$', register, name='register'),
    url(r'logout$', logout, name='logout')
]