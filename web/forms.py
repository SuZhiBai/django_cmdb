#coding:utf-8
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label=u'用户名',error_messages={'required':u'用户名不能为空'})
    email = forms.EmailField(label=u'邮箱',error_messages={'required': u'邮箱不能为空'} )
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
class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名',error_messages={'required':u'用户名不能为空'})
    password = forms.CharField(
        label=(u'密码'),
        widget=forms.PasswordInput,
        error_messages={'required': u'密码不能为空'}
    )