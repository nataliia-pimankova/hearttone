# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import Patient

def records_list(request):
    return render(request, 'records/records_list.html', {})


def records_add(request):
    return render(request, 'records/records_add.html', {})


def records_edit(request):
    return render(request, 'records/records_add.html', {})


# Views for Groups
class PatientList(ListView):
    model = Patient
    context_object_name = 'records'
    template_name = 'records/records_list.html'

    # def get_context_data(self, **kwargs):
    #     """This method adds extra variables to template"""
    #     # get original context data from parent class
    #     context = super(PatientList, self).get_context_data(**kwargs)
    #
    #     patients = Patient.objects.all()
    #
    #
    #     context['patients']
    #     # return context mapping
    #     return context

