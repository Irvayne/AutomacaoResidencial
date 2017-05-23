from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  
  url(r'^$', 'residencial.views.login', name='login'),
  url(r'^dashboard/$', 'residencial.views.home', name='home'),
  url(r'^dashboard/conforto$', 'residencial.views.conforto', name='conforto'),
  url(r'^liga1/$', 'residencial.views.liga1', name='liga1'),
  url(r'^liga2/$', 'residencial.views.liga2', name='liga2'),
  url(r'^liga3/$', 'residencial.views.liga3', name='liga3'),
  url(r'^liga4/$', 'residencial.views.liga4', name='liga4'),
  url(r'^liga5/$', 'residencial.views.liga5', name='liga5'),
  url(r'^liga6/$', 'residencial.views.liga6', name='liga6'),
  url(r'^liga7/$', 'residencial.views.liga7', name='liga7'),
  url(r'^liga8/$', 'residencial.views.liga8', name='liga8'),
  url(r'^desliga1/$', 'residencial.views.desliga1', name='desliga1'),
  url(r'^desliga2/$', 'residencial.views.desliga2', name='desliga2'),
  url(r'^desliga3/$', 'residencial.views.desliga3', name='desliga3'),
  url(r'^desliga4/$', 'residencial.views.desliga4', name='desliga4'),
  url(r'^desliga5/$', 'residencial.views.desliga5', name='desliga5'),
  url(r'^desliga6/$', 'residencial.views.desliga6', name='desliga6'),
  url(r'^desliga7/$', 'residencial.views.desliga7', name='desliga7'),
  url(r'^desliga8/$', 'residencial.views.desliga8', name='desliga8'),
  url(r'^dashboard/economia$', 'residencial.views.economia', name='economia')
  


)
