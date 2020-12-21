from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')


# 返回子页面
def child(request,eid,oid):
    return render(request,eid)


def home(request):
    return render(request,'welcome.html',{"whichHTML":"home.html","oid":""})


