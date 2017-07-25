from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'results$', results, name='results'),
    url(r'process$', process,name='process'),
    ]