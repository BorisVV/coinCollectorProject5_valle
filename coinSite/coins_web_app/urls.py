from django.conf.urls import url # patternsas
from . import views # local file

urlpatterns = [
url(r'^$', views.index, name='index')
]
