# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import expense,income,Token

# Register your models here.
admin.site.register(expense)
admin.site.register(income)

admin.site.register(Token)
