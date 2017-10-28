# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def records_list(request):
    return render(request, 'records/records_list.html', {})


def records_add(request):
    return render(request, 'records/records_add.html', {})