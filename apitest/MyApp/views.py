from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
# Create your views here.

def welcome(request):
    return render(request,'welcome.html',{"whichHTML":"home.html","oid":""})



# 返回子页面
def child(request,eid,oid):
    return render(request,eid)


def home(request):
    return render(request,'welcome.html',{"whichHTML":"home.html","oid":""})

def login(request):
    return render(request,'login.html')

def login_action(request):
    # 获取前端传递的数据
    u_name = request.GET['username']
    p_word = request.GET['password']
    print(u_name,p_word)

    # 利用django中的auth库对数据库中的用户信息进行验证,正确返回用户实体，错误返回None
    user = auth.authenticate(username=u_name,password=p_word)
    if user is not None:
        # 重定向进入登录页
        return HttpResponseRedirect('/home/')
    else:
        # 返回前端信息，用户密码不正确
        return HttpResponse('您的用户名密码不正确')