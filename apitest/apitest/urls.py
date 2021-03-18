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
    url(r'^accounts/login/$', login),  # 非登录态自动跳回登录页面

    # 返回子菜单
    url(r'^child/(?P<eid>.+)/(?P<oid>.*)/$',child)
]