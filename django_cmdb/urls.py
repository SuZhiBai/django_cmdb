#coding:utf-8
"""my8 URL Configuration

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

'''
url对应具体的方法-------------
url(r'^index/',index),
#动态路由,最后加上/后，访问时会自动补全/，否则不补全
url(r'^list/(\d*)/',list),
#name为对应view里参数的名字
url(r'^listname/(?P<name>\d*)/',listname),
'''
#url做全局路由，路由至每个APP内部处理
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/',include('web.urls',namespace="web")),

]