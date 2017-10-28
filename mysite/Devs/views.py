# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render,HttpResponse,loader,redirect,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from .models import developers
from .models import trusts,post,comment
from .forms import registrationform,commentform
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.utils import timezone




# Create your views here.
def home(request):
    return render(request,'home.html')
def index(request):
    all_developers = developers.objects.all()

    context = {'all_developers' : all_developers}
    return render(request,'index.html',context)

class Indexview(generic.ListView):
    template_name='trusts.html'
    context_object_name='all_trusts'
    def get_queryset(self):
        return trusts.objects.all()

class posts(generic.ListView):
    template_name='posts.html'
    context_object_name='all_post'
    def get_queryset(self):
        return post.objects.all()



class voluntersview(generic.ListView):
    template_name='volunters.html'
    context_object_name='all_users'
    def get_queryset(self):
        return User.objects.all()

class trustscreate(CreateView):
    model = trusts
    fields =['name','contact_num','Street_Address','Locality']
class postcreate(CreateView):
    """docstring forpostcreate."""
    model=post
    fields =['title','location','Address','content','author']

class comment(CreateView):
    """docstring forpostcreate."""
    model=comment
    fields =['content']

def register(request):
    if request.method =="POST":
      form=registrationform(request.POST)
      if form.is_valid():
          user=form.save()
          user.refresh_from_db()  # load the profile instance created by the signal
          user.save()
          raw_password = form.cleaned_data.get('password1')
          user1 = authenticate(username=user.username, password=raw_password)
          login(request, user1)
          return redirect('Devs:posts')
    else :
      form=registrationform()
      args ={'form':form}
      return render(request,'Devs/reg_form.html',args)
def profile(request):
    args = {'user':request.user}
    return render(request,'profile.html',args)
def postdetail(request, post_id):
    return render(request, 'postdetail.html', {'post': post.objects.get(pk=post_id)})
def createcomment(request, post_id):
    if request.method =="POST":
      form=commentform(request.POST)
      post1=post.objects.get(pk=post_id)
      if form.is_valid():
          comment=form.save(commit=False)
          comment.post=post1
          comment.user1=request.user
          comment.date=timezone.now()
          comment.save()
          return redirect('Devs:postdetail',post_id)
    else :
      form=commentform()
      args ={'form':form}
      return render(request,'Devs/comment_form.html',args)
