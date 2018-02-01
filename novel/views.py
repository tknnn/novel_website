# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import * #NovelCope
# Create your views here.

def index(request):
    #novelcopy = NovelCopy.object.get(novelid=1) #查数据 get查询单条数据
    novelcopy = NovelCopy.object.filter().order_by('?')[:4] #随机取4个
    context = {
        'novels':1,

    }
    return render(request, 'index.html', context=context)