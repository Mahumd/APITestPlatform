from django.contrib import admin

# Register your models here.
#导入所有的表结构
from MyApp.models import *
# 注册吐槽表
admin.site.register(DB_tucao)