from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'search$', search, name='search'),
    url(r'results$', results, name='results'),
    url(r'listing/start$', start_listing, name='start_listing'),
    url(r'listing/new$', gather_info, name='info'),
]