# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import developers,trusts,post,comment

admin.site.register(developers)
admin.site.register(trusts)
admin.site.register(post)
admin.site.register(comment)

# Register your models here.
