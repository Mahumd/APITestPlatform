from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from MyApp.models import *


# Create your views here.
@login_required()
def welcome(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


# 控制不同的页面返回不同的数据：数据分发器
def child_json(eid, oid=''):
    # 获取所有的超链接信息
    res = {}
    if eid == "home.html":
        date = DB_home_href.objects.all()
        res = {"hrefs": date}
    if eid == "project_list.html":
        date = DB_project_list.objects.all()
        res = {"projects": date}
    if eid == 'P_apis.html':
        project_name = DB_project_list.objects.filter(id=oid)[0].name
        res = {"project_name": project_name}
    return res


# 返回子页面
def child(request, eid, oid):
    # 获取所有的超链接列表
    res = child_json(eid, oid)
    return render(request, eid, res)


@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


def login(request):
    return render(request, 'login.html')


def accounts_login(request):
    return HttpResponseRedirect('/login/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def login_action(request):
    # 获取前端传递的数据
    u_name = request.GET['username']
    p_word = request.GET['password']
    # print(u_name,p_word)

    # 利用django中的auth库对数据库中的用户信息进行验证,正确返回用户实体，错误返回None
    user = auth.authenticate(username=u_name, password=p_word)
    print(user)
    if user is not None:
        auth.login(request, user)
        request.session['user'] = u_name
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
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse('成功')
    except:
        return HttpResponse('失败')


def tucao_send(request):
    # 后端获取前端传递的吐槽的内容
    tucao_text = request.GET['tucao_text']
    print(tucao_text)
    # 将吐槽的内容写入数据库当中
    DB_tucao.objects.create(user=request.user.username, text=tucao_text)
    # 返回给前端一个值，表示入库成功
    return HttpResponse('成功')


def help_info(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})


def project_list(request):
    return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})


def delete_project(request):
    id = request.GET['id']
    DB_project_list.objects.filter(id=id).delete()
    return HttpResponse('')


def add_project(request):
    project_name = request.GET['project_name']
    DB_project_list.objects.create(name=project_name, remark='', user=request.user.username, other_user='')
    return HttpResponse('')


def open_apis(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_apis.html", "oid": project_id})
