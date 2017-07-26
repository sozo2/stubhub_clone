from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'results$', results, name='results'),
    url(r'process$', process, name='process'),
    url(r'ticket_change$', ticket_change, name='ticket_change'),
    url(r'event/(?P<event_id>\d+)$', event, name='event'),
    url(r'event/(?P<event_id>\d+)/(?P<sort_by>[A-z]+)$', event, name='event'),
    ]