from django.contrib import admin
from django.conf.urls import url, include
from.import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'about', views.about, name='about'),
    url(r'contactus', views.contactus, name='contactus'),

]
