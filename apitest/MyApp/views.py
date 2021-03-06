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
        project = DB_project_list.objects.filter(id=oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res = {"project": project, "apis": apis}
        # print(res)
    if eid == 'P_cases.html':
        project = DB_project_list.objects.filter(id=oid)[0]
        res = {"project": project}
    if eid == 'P_project_set.html':
        project = DB_project_list.objects.filter(id=oid)[0]
        res = {"project": project}

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


def open_cases(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_cases.html", "oid": project_id})


def open_project_set(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "P_project_set.html", "oid": project_id})


def project_id_add(request, pid):
    project_id = pid
    # print(project_id)
    DB_apis.objects.create(project_id=project_id)
    return HttpResponseRedirect('/apis/%s' % project_id)


def project_id_del(request, id):
    project_id = DB_apis.objects.filter(id=id)[0].project_id
    # print(project_id)
    DB_apis.objects.filter(id=id).delete()
    return HttpResponseRedirect('/apis/%s' % project_id)


def save_bz(request):
    id = request.GET['api_id']
    bz_value = request.GET['bz_value']

    # print(bz_value)
    DB_apis.objects.filter(id=id).update(desc=bz_value)
    return HttpResponse('')


def get_bz(request):
    id = request.GET['api_id']
    bz_value = DB_apis.objects.filter(id=id)[0].desc
    return HttpResponse(bz_value)


def Api_save(request):
    # 提取所有的数据
    api_id = request.GET['api_id']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']
    ts_api_body = request.GET['ts_api_body']
    # 保存数据到数据库中
    DB_apis.objects.filter(id=api_id).update(
        api_method = ts_method,
        api_url = ts_url,
        api_host = ts_host,
        api_header = ts_header,
        body_method = ts_body_method,
        api_body = ts_api_body
    )
    # 返回
    return HttpResponse('success')
