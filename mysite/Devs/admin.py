# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import developers,trusts

admin.site.register(developers)
admin.site.register(trusts)

# Register your models here.
