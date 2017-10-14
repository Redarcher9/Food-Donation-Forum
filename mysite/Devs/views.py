# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render,HttpResponse,loader
from .models import developers



# Create your views here.
def index(request):
    all_developers = developers.objects.all()

    context = {'all_developers' : all_developers}
    return render(request,'Devs/index.html',context)
