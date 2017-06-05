"""
Define the url mapping for catalog app

"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
