#coding:utf-8
from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Gender = models.BooleanField(default=False)
    Age = models.IntegerField(default=20)
    memo = models.TextField(default='tomxxx')
    CreatDate = models.DateTimeField(default='2015-08-08 08:08')
    typeId = models.ForeignKey('UserType',default=1)

class UserType(models.Model):
    name = models.CharField(max_length=50)

#多对多关系
class Group(models.Model):
    Name = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    group_relation = models.ManyToManyField('Group')
    def __unicode__(self):
        return self.username

#自动修改时间
class Asset(models.Model):
    hostname = models.CharField(max_length=50,null=False)
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
