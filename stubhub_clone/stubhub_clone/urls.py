"""stubhub_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include("apps.main.urls", namespace='main')),
    url(r'^login', include("apps.login_reg.urls", namespace='login')),
    url(r'^my_hub', include("apps.my_hub.urls", namespace='my_hub')),
    #url(r'^checkout', include("apps.checkout.urls"), name='checkout'),
    url(r'^search', include("apps.find_tickets.urls"), name='search'),
    # url(r'^sell_tickets', include("apps.sell_tickets.urls"), name='sell_tickets'),
    # url(r'^admin/', admin.site.urls),
]
