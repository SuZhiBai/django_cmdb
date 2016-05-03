#coding:utf-8
from django import forms
from models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label=u'用户名',error_messages={'required':u'用户名不能为空'})
    email = forms.EmailField(label=u'邮箱',error_messages={'required': u'邮箱不能为空','invalid':u'邮箱格式错误'} )
    password_1 = forms.CharField(
        label=(u'密码'),
        widget=forms.PasswordInput,
        error_messages={'required': u'密码不能为空'}
    )
    password_2 = forms.CharField(
        label=(u'确认密码'),
        widget=forms.PasswordInput,
        error_messages={'required': u'密码不能为空'}
    )
    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError(('两次密码不同，请确认'))
        return password_2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_email_exist = User.objects.filter(email=email).exists()
        if is_email_exist:
            raise forms.ValidationError(u'该邮箱已被注册')
        return email
    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_username_exist = User.objects.filter(username=username).exists()
        if is_username_exist:
            raise forms.ValidationError(u'该用户名已被注册')
        return username

class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名',error_messages={'required':u'用户名不能为空'})
    password = forms.CharField(
        label=(u'密码'),
        widget=forms.PasswordInput,
        error_messages={'required': u'密码不能为空'}
    )

class HostForm(forms.Form):
    hostname = forms.IPAddressField(label=(u'设备IP'))
    hostroom = forms.CharField(label=(u'机房名称'))
    racknum = forms.CharField(label=(u'机架编号'))
    equmodel = forms.CharField(label=(u'设备型号'))
    personin = forms.CharField(label=(u'负责人'))

class HostRoomForm(forms.Form):
    id =forms.IntegerField(label='机房ID',widget = forms.HiddenInput())
    roomname = forms.IPAddressField(label=(u'机房名称'))
    roomcity = forms.IPAddressField(label=(u'城市名称'))
    isp = forms.IPAddressField(label=(u'运营商名称'))
    tradename = forms.IPAddressField(label=(u'厂商名称'))
    contacts = forms.IPAddressField(label=(u'联系人'))
    telephone = forms.IntegerField(label=(u'联系电话'))