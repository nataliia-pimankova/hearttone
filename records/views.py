# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib import messages
from django.db import transaction
from django.forms.models import inlineformset_factory

from .models import Patient, Record
from .forms import PatientCreateForm, PatientUpdateForm, PatientForm, RecordForm


def records_list(request):
    return render(request, 'records/records_list.html', {})


def records_add(request):
    return render(request, 'records/records_add.html', {})


def records_edit(request):
    return render(request, 'records/records_add.html', {})


# Views for Groups
class PatientList(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'records/records_list.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(PatientList, self).get_context_data(**kwargs)

        patients = Patient.objects.all()
        for patient in patients:
            patient.records = Record.objects.filter(patient_id=patient.pk)

        context['patients'] = patients

        return context


def edit_patient(request, id_patient=None):
    if id_patient is None:
        patient = Patient()
        RecordInlineFormSet = inlineformset_factory(Patient, Record, form=RecordForm, extra=1, can_delete=False)
    else:
        patient = Patient.objects.get(pk=id_patient)
        RecordInlineFormSet = inlineformset_factory(Patient, Record, form=RecordForm, extra=0, can_delete=True)

    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES, instance=patient, prefix="main")
        formset = RecordInlineFormSet(request.POST, request.FILES, instance=patient, prefix="nested")

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient, prefix="main")
        formset = RecordInlineFormSet(instance=patient, prefix="nested")

    return render(request, "records/patient_edit.html", {"form": form, "formset": formset})


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreateForm
    template_name = 'records/templates_add_edit.html'

    def get_success_url(self):
        messages.success(self.request, u"Patient added successfully!")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, u'Patient addition canceled!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(PatientCreateView, self).post(request, *args, **kwargs)


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientUpdateForm
    template_name = 'records/templates_add_edit.html'

    def get_success_url(self):
        messages.success(self.request, u"Patient saved successfully!")
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, u'Patient edition canceled!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(PatientUpdateView, self).post(request, *args, **kwargs)


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'records/record_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, u"Patient deleted successfully!")
        return reverse('home')


class PatientRecordCreateView(CreateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'records/patient_form.html'

    def get_context_data(self, **kwargs):
        context = super(PatientRecordCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['records'] = RecordFormSet(self.request.POST)
        else:
            context['records'] = RecordFormSet()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        records = context['records']
        with transaction.atomic():
            self.object = form.save()

            if records.is_valid():
                records.instance = self.object
                records.save()

        return super(PatientRecordCreateView, self).form_valid(form)


class PatientRecordUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'records/patient_form.html'

    def get_context_data(self, **kwargs):
        context = super(PatientRecordUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['records'] = RecordFormSet(self.request.POST)
        else:
            context['records'] = RecordFormSet()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        records = context['records']
        with transaction.atomic():
            self.object = form.save()

            if records.is_valid():
                records.instance = self.object
                records.save()

        return super(PatientRecordUpdateView, self).form_valid(form)
