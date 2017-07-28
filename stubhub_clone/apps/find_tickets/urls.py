from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'results$', results, name='results'),
    url(r'process$', process, name='process'),
    url(r'ticket_change$', ticket_change, name='ticket_change'),
    url(r'tickets/(?P<event_id>\d+)$', tickets, name='tickets'),
    url(r'ticketspass/(?P<event_id>\d+)/(?P<tickets>\d+)$', ticketspass, name='ticketspass'),
    url(r'event/(?P<event_id>\d+)$', event, name='event'),
    url(r'event/(?P<event_id>\d+)/(?P<sort_by>[A-z]+)$', event, name='event'),
    url(r'venue/(?P<venue_id>\d+)$', venue, name='venue'),
    url(r'performer/(?P<performer_id>\d+)$', performer, name='performer'),
    ]