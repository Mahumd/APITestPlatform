from django.contrib import admin

# Register your models here.
# 导入所有的表结构
from MyApp.models import *

# 注册吐槽表
admin.site.register(DB_tucao)

# 注册传送门路径表
admin.site.register(DB_home_href)

# 注册项目表
admin.site.register(DB_project_list)
