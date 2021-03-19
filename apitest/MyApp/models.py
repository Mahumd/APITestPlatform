from django.db import models

# Create your models here.

class DB_tucao(models.Model):
    #id--默认
    #吐槽人姓名
    user = models.CharField(max_length=30,null=True)
    #吐槽人内容
    text = models.CharField(max_length=1000,null=True)
    #吐槽时间
    ctime = models.DateTimeField(auto_now=True)

    #页面中需要展示的数据
    def __str__(self):
        return self.text+str(self.ctime)