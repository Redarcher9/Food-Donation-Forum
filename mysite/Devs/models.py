# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.db import models


# Create your models here.
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
