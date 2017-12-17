from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.loginSubmit),
    url(r'^register$', views.registerSubmit),
    url(r'^registerPage', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboardTwo', views.dashboardTwo),
    url(r'^studySession', views.studySession),
    url(r'^registerSubmit', views.registerSubmitInRegisterPage),
    url(r'^connect', views.connect),
    url(r'^findPartner', views.findPartner),
    url(r'^logout', views.logout),
]
