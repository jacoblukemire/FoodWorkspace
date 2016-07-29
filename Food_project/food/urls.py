from django.conf.urls import patterns, url
from food import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_fooditem/$', views.add_fooditem, name='add_fooditem'), # NEW MAPPING!
        url(r'^add_foodentry/$', views.add_foodentry, name='add_foodentry'), # NEW MAPPING!
        url(r'^restricted/', views.restricted, name='restricted'),
)
