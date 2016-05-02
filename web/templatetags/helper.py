#coding:utf-8
from django import template
from django.template.base import resolve_variable,NodeList
from bootstrapform.templatetags import bootstrap

#初始化一个template对象
register = template.Library()

@register.simple_tag
def mymethod(v1):
    result = v1*1000
    return result