from django.conf.urls import url, include # patterns
from . import views

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quarters$', views.quarters_list, name='quarters_list'),
    url(r'^login$', login, {'template_name': 'coins_web_app/login.html'})
    ]
