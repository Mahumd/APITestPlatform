from django.db import models


# Create your models here.

# 吐槽记录
class DB_tucao(models.Model):
    # id--默认
    # 吐槽人姓名
    user = models.CharField(max_length=30, null=True)
    # 吐槽人内容
    text = models.CharField(max_length=1000, null=True)
    # 吐槽时间
    ctime = models.DateTimeField(auto_now=True)

    # 页面中需要展示的数据
    def __str__(self):
        return self.text + str(self.ctime)


# 传送门
class DB_home_href(models.Model):
    # 超链接名称
    name = models.CharField(max_length=30, null=True)
    # 超链接地址
    href = models.CharField(max_length=3000, null=True)

    # 前端显示超链接名称
    def __str__(self):
        return self.name


# 项目列表
class DB_project_list(models.Model):
    # 项目
    name = models.CharField(max_length=100, null=True)
    # 备注
    remark = models.CharField(max_length=1000, null=True)
    # 项目创建人
    user = models.CharField(max_length=15, null=True)
    # 项目其他创建人
    other_user = models.CharField(max_length=200, null=True)

    # 前端展示的项目名
    def __str__(self):
        return self.name


# 接口库
class DB_apis(models.Model):
    # 项目id
    project_id = models.CharField(max_length=10, null=True)
    # 接口名字
    name = models.CharField(max_length=100, null=True)
    # 请求方式
    api_method = models.CharField(max_length=10, null=True)
    # URL
    api_url = models.CharField(max_length=1000, null=True)
    # 请求头
    api_header = models.CharField(max_length=1000, null=True)
    # 是否带登录态
    api_login = models.CharField(max_length=10, null=True)
    # 域名
    api_host = models.CharField(max_length=100, null=True)
    # 描述
    desc = models.CharField(max_length=100, null=True)
    # 请求体编码格式
    body_method = models.CharField(max_length=30, null=True)
    # 请求体
    api_body = models.CharField(max_length=1000, null=True)
    # 返回体
    result = models.CharField(max_length=1000, null=True)
    # 是否验签
    sign = models.CharField(max_length=10, null=True)
    # 文件key
    file_key = models.CharField(max_length=50, null=True)
    # 文件名
    file_name = models.CharField(max_length=50, null=True)
    # 全局变量-请求头
    public_hearder = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name
