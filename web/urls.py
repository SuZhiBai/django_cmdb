#coding:utf-8
"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web.views import index,Register,Login,HostList,AddHost,HostRoomList,AddHostRoom,TableList,DelHostRoom,UpdateHostRoom

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$',Login,name='login'),
    url(r'^register/$',Register,name='register'),
    url(r'^hostlist/$', HostList, name='hostlist'),
    url(r'^hostroomlist/$', HostRoomList, name='hostroomlist'),
    url(r'^tablelist/$',TableList, name='tablelist'),
    url(r'^addhost/$',AddHost,name='addhost'),
    url(r'^addhostroom/$', AddHostRoom, name='addhostroom'),
    url(r'^delhostroom/$', DelHostRoom, name='delhostroom'),
    url(r'^updatehostroom/$', UpdateHostRoom, name='updatehostroom'),

]
