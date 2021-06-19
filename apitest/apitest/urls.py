"""apitest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApp.views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/$', welcome),  # 获取菜单
    url(r'^$', home),
    url(r'^home/$', home),  # 进入首页
    url(r'^login/$', login),  # 进入登录页
    url(r'^logout/$', logout),  # 退出
    url(r'^login_action/$', login_action),  # 登录
    url(r'^register_action/$', register_action),  # 注册
    url(r'^accounts/login/$', accounts_login),  # 非登录态自动跳回登录页面
    url(r'^tucao_send/$', tucao_send),  # 反馈
    url(r'^help/$', help_info),  # 帮助
    url(r'^project_list/$', project_list),  # 进入项目列表
    url(r'^delete_project/$', delete_project),  # 删除项目
    url(r'^add_project/$', add_project),  # 新增项目
    url(r'^apis/(?P<id>.*)/$', open_apis),  # 进入接口库
    url(r'^cases/(?P<id>.*)/$', open_cases),  # 进入用例库
    url(r'^project_set/(?P<id>.*)/$', open_project_set),  # 进入项目设置
    url(r'^project_api_add/(?P<pid>.*)/$', project_id_add),  # 新增接口
    url(r'^project_api_del/(?P<id>.*)/$', project_id_del),  # 删除接口
    url(r'^save_bz/$', save_bz),  # 保存备注
    url(r'^get_bz/$', get_bz),  # 获取备注

    # 返回子菜单
    url(r'^child/(?P<eid>.+)/(?P<oid>.*)/$',child)
]