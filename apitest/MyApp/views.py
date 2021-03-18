from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def welcome(request):
    return render(request,'welcome.html',{"whichHTML":"home.html","oid":""})



# 返回子页面
def child(request,eid,oid):
    return render(request,eid)

@login_required
def home(request):
    return render(request,'welcome.html',{"whichHTML":"home.html","oid":""})

def login(request):
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def login_action(request):
    # 获取前端传递的数据
    u_name = request.GET['username']
    p_word = request.GET['password']
    # print(u_name,p_word)

    # 利用django中的auth库对数据库中的用户信息进行验证,正确返回用户实体，错误返回None
    user = auth.authenticate(username=u_name,password=p_word)
    print(user)
    if user is not None:
        auth.login(request,user)
        request.session['user']=u_name
        # # 重定向进入登录页
        # return HttpResponseRedirect('/home/')
        return HttpResponse('成功')
    else:
        # 返回前端信息，用户密码不正确
        return HttpResponse('失败')

def register_action(request):
    # 获取前端传递的数据
    u_name = request.GET['username']
    p_word = request.GET['password']

    try:
        # 将输入的用户名密码保存到数据库中
        user = User.objects.create_user(username=u_name,password=p_word)
        user.save()
        return HttpResponse('成功')
    except:
        return HttpResponse('失败')
def tucao_send(request):
    pass
