# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib import messages

from .models import Patient
from .forms import RecordCreateForm, RecordUpdateForm


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


class RecordCreateView(CreateView):
    model = Patient
    form_class = RecordCreateForm
    template_name = 'records/templates_add_edit.html'

    def get_success_url(self):
        messages.success(self.request, u"Record added successfully!")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, u'Record addition canceled!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(RecordCreateView, self).post(request,*args,**kwargs)


class RecordUpdateView(UpdateView):
    model = Patient
    form_class = RecordUpdateForm
    template_name = 'records/templates_add_edit.html'

    def get_success_url(self):
        messages.success(self.request, u"Record saved successfully!")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, u'Record edition canceled!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(RecordUpdateView, self).post(request,*args,**kwargs)


class RecordDeleteView(DeleteView):
    model = Patient
    template_name = 'records/record_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, u"Record deleted successfully!")
        return reverse('home')

