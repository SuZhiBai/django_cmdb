#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.http.response import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from web.models import Asset,User
from web.forms import RegisterForm,LoginForm

def Register(request):
    registerForm = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password_1']
            user = User.objects.create(
                username=username,
                email=email,
                password=password)
            user.save()
            return redirect(reverse('web:index'))
        else:
            temp = form.errors.as_data()
            print temp
            return render_to_response('register.html',{'form':form},context_instance = RequestContext(request))
            #return redirect(reverse("web:register"))

    return render_to_response('register.html',{'form':registerForm},
            context_instance = RequestContext(request)
            )

def login(request):
    loginForm = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = User.objects.filter(
                username=username,
                password=password).count()
            if user == 1:
                return redirect(reverse('web:index'))
        else:
            temp = form.errors.as_data()
            print temp
            return render_to_response('login.html',{'form': form}, context_instance=RequestContext(request))
    return render_to_response('login.html',{'form': loginForm}, context_instance=RequestContext(request))

def index(request):
    return  render_to_response('index.html')