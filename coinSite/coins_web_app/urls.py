from django.conf.urls import url, include # patterns
from . import views # local file

urlpatterns = [
url(r'^$', views.index, name='index')
]
