#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.hashers import make_password
from django.utils.safestring import mark_safe
from django.http.response import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from web.models import User,UserType,Host,HostRoom
from web.forms import RegisterForm,LoginForm,HostForm,HostRoomForm
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Q
import json

def Register(request):
    registerForm = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #UserType.objects.filter(id=2) 获取结果是对象会报错，而get到的是一个实例
        ut = UserType.objects.get(id=2)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password_1']
            user = User.objects.create(
                username = username,
                email = email,
                password = make_password(password,'test','pbkdf2_sha256'),
                usertype = ut
            )
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

def Login(request):
    loginForm = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            print make_password(password,'test','pbkdf2_sha256')
            user = User.objects.filter(
                username=username,
                password=make_password(password,'test','pbkdf2_sha256')).count()
            if user == 1:
                return redirect(reverse('web:index'))
            else:
                return render_to_response('login.html', {'form': form,'message':u'用户或密码错误'},
                                          context_instance=RequestContext(request))
        else:
            temp = form.errors.as_data()
            print temp
            return render_to_response('login.html',{'form': form}, context_instance=RequestContext(request))
    return render_to_response('login.html',{'form': loginForm}, context_instance=RequestContext(request))

def index(request):
    return  render_to_response('index.html')
def HostList(request):
    return render_to_response('hostlist.html',{'hostform':HostForm},context_instance=RequestContext(request))

def HostRoomList(request):
    #idcs = HostRoom.objects.all()
    return render_to_response('hostroomlist.html',{'hostroomform':HostRoomForm},
                              context_instance=RequestContext(request))
def TableList(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    search = request.GET.get('search',None)
    if not search or search is  None:
        total = HostRoom.objects.all().count()
        sp = int(offset)
        ep = int(limit)+int(offset)
        data_json_r = serializers.serialize("json", HostRoom.objects.all()[sp:ep])
    else:
        data_search = HostRoom.objects.filter(Q(contacts__icontains=search)|Q(roomname__icontains=search)|
                                              Q(roomcity__icontains=search)|Q(isp__icontains=search)|
                                              Q(tradename__icontains=search)|Q(telephone__icontains=search))
        data_json_r = serializers.serialize("json",data_search)
        total = data_search.count()
    data_list_r = json.loads(data_json_r)
    data_list = []
    for data in data_list_r:
        tmp = data['fields']
        tmp['id'] = HostRoom.objects.get(roomname=tmp['roomname']).id
        data_list.append(tmp)
    data = {'total':total,'rows':data_list}
    return HttpResponse(json.dumps(data))

def AddHost(request):
    hostform = HostForm()
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data['hostname']
            hostroom = form.cleaned_data['hostroom']
            Host.objects.create(hostname=hostname,hostroom=hostroom)
        else:
            return render_to_response('hostlist.html', {'form': form, 'message': u'输入信息错误'},
                                      context_instance=RequestContext(request))
    return render_to_response('hostlist.html', {'form': hostform},
                                  context_instance=RequestContext(request))
@csrf_exempt
def AddHostRoom(request):
    result = {'status': 0,'msg':'成功','data':'---ok---'}
    if request.is_ajax():
        roomname = request.POST.get('roomname')
        roomcity = request.POST.get('roomcity')
        isp = request.POST.get('isp')
        tradename = request.POST.get('tradename')
        contacts = request.POST.get('contacts')
        telephone = request.POST.get('telephone')
        print roomname,roomcity
        if all([roomname,roomcity,isp,tradename,contacts,telephone]):
            try:
                HostRoom.objects.create(roomname=roomname,roomcity=roomcity,
                                    isp=isp,tradename=tradename,contacts=contacts,telephone=telephone)
            except:
                print u'数据添加失败'
            else:
                result['status'] = 1
    print result['status']
    return HttpResponse(json.dumps(result))


@csrf_exempt
def DelHostRoom(request):
    result = {'status': 0,'msg':'成功','data':'ok'}
    if request.is_ajax():
        roomname = request.POST.get('roomname')
        if roomname:
            try:
                HostRoom.objects.filter(roomname=roomname).delete()
            except:
                print u'删除数据失败'
            else:
                result['status'] = 1
    return HttpResponse(json.dumps(result))

@csrf_exempt
def UpdateHostRoom(request):
    result = {'status': 0,'msg':'成功','data':'---ok---'}
    if request.is_ajax():
        id = request.POST.get('id')
        roomname = request.POST.get('roomname')
        roomcity = request.POST.get('roomcity')
        isp = request.POST.get('isp')
        tradename = request.POST.get('tradename')
        contacts = request.POST.get('contacts')
        telephone = request.POST.get('telephone')
        if all([roomname,roomcity,isp,tradename,contacts,telephone]):
            try:
                HostRoom.objects.filter(id=id).update(roomname=roomname,roomcity=roomcity,
                                    isp=isp,tradename=tradename,contacts=contacts,telephone=telephone)
            except:
                print u'数据编辑失败'
            else:
                result['status'] = 1
    return HttpResponse(json.dumps(result))