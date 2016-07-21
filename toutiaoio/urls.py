# codding: utf-8
from django.conf.urls import include, url
import toutiaoio.views as views

urlpatterns = [
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/*$', views.index, name="index"),

    url(r'', views.index),
]