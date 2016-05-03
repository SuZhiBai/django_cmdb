#coding:utf-8
from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    #对应为UserType表的一个对象
    usertype = models.ForeignKey('UserType')
    def __unicode__(self):
        return self.username

# 多对多关系
class HostRoom(models.Model):
    roomname = models.CharField(max_length=50,unique=True)
    roomcity = models.CharField(max_length=50)
    isp = models.CharField(max_length=50)
    tradename = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)
    telephone = models.BigIntegerField()

#自动修改时间
class Host(models.Model):
    hostname = models.IPAddressField(unique=True)
    hostroom = models.ForeignKey('HostRoom')
    racknum = models.CharField(max_length=50)
    equmodel = models.CharField(max_length=50)
    personin = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

#不需要再创建表
class User_Temp(models.Model):
    GENDER_CHOICE = (
        (u'1',u'普通用户'),
        (u'2',u'管理员'),
        (u'3',u'超级管理员'),
    )
    UserType = models.CharField(max_length=20,choices=GENDER_CHOICE)
