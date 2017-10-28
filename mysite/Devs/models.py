# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models


# Create your models here.
class post(models.Model):
    """docstring forpost."""
    title = models.CharField(max_length=250,null=True, blank=True)
    location = models.CharField(max_length=250)
    Address =  models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User,null=True, blank=True)
    author = models.CharField(max_length=250,null=True, blank=True)
    date=models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse('Devs:posts')

class comment(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    context = models.CharField(max_length=1000)
    user1=models.ForeignKey(User)
    date=models.DateTimeField(auto_now=True)


class developers(models.Model):
    name = models.CharField(max_length=250)
    contact_num = models.CharField(max_length=250)
    email = models.CharField(max_length=500)
    Designation = models.CharField(max_length=500)
    photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + '-' + self.Designation


class trusts(models.Model):
    name=models.CharField(max_length=250)
    contact_num=models.CharField(max_length=250)
    Street_Address=models.CharField(max_length=500)
    Locality=models.CharField(max_length=250)

    def __str__(self):
        return self.name + '-' +self.Locality
    def get_absolute_url(self):
        return reverse('Devs:trusts')
