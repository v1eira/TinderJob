from django.urls import path
from .views import views

#urlpatterns = [
#    path('', views.candidatos_list, name='candidatos_list'),
#]

##
# from django.conf.urls import patterns, include, url

#urlpatterns = patterns('',
#    url(r'', "views.home"),
#)

urlpatterns = [
    path('', views.home, name='home'),
]