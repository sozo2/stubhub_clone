from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', login_reg),
    url(r'^/authenticate$', authenticate),
    url(r'^/register$', register),

]