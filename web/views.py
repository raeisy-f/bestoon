# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def submit_expense(request):
    """user submits and expense"""
    return request.POST
