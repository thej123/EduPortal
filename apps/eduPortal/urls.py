from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register', views.register),
    url(r'^dashboard', views.dashboard),
    url(r'^registerSubmit', views.registerSubmit),
    url(r'^connect', views.connect),
    url(r'^findPartner', views.findPartner),
]
