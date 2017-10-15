# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render,HttpResponse,loader
from django.views import generic
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from .models import developers
from .models import trusts



# Create your views here.
def index(request):
    all_developers = developers.objects.all()

    context = {'all_developers' : all_developers}
    return render(request,'Devs/index.html',context)

class Indexview(generic.ListView):
    template_name='Devs/trusts.html'
    context_object_name='all_trusts'
    def get_queryset(self):
        return trusts.objects.all()


class trustscreate(CreateView):
    model = trusts
    fields =['name','contact_num','Street_Address','Locality']
