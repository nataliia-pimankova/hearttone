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
from .forms import PatientCreateForm, PatientUpdateForm, PatientForm, RecordInlineForm


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
        RecordInlineFormSet = inlineformset_factory(Patient, Record, form=RecordInlineForm, extra=1, can_delete=False)
    else:
        patient = Patient.objects.get(pk=id_patient)
        if Record.objects.filter(patient_id=id_patient):
            RecordInlineFormSet = inlineformset_factory(Patient, Record, form=RecordInlineForm, extra=0, can_delete=True)
        else:
            RecordInlineFormSet = inlineformset_factory(Patient, Record, form=RecordInlineForm, extra=1, can_delete=True)

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

PatientInlineFormSet = inlineformset_factory(
    Patient,
    Record,
    form=RecordInlineForm,
    extra=1,
    can_delete=False,
    can_order=False
)


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreateForm
    template_name = 'records/templates_add_edit.html'

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(PatientCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = PatientForm(self.request.POST)
            ctx['formset'] = PatientInlineFormSet(self.request.POST)
        else:
            ctx['form'] = Patient()
            ctx['formset'] = PatientInlineFormSet()
        return ctx

    def get_success_url(self):
        messages.success(self.request, u"Patient added successfully!")
        return reverse('home')

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['formset']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save() # saves Father and Children
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

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
    form_class = PatientCreateForm
    # fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'records/patient_edit.html'

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(PatientRecordCreateView, self).get_context_data(**kwargs)

        patient = Patient()
        RecordInlineFormSet = inlineformset_factory(Patient, Record, form=RecordInlineForm, extra=1, can_delete=False)

        if self.request.method == "POST":
            ctx['form'] = PatientCreateForm(self.request.POST, self.request.FILES, instance=patient, prefix="main")
            self.formset = RecordInlineFormSet(self.request.POST, self.request.FILES, instance=patient, prefix="nested")
        else:
            ctx['form'] = PatientCreateForm(instance=patient, prefix="main")
            self.formset = RecordInlineFormSet(instance=patient, prefix="nested")

        # if self.request.POST:
        #     ctx['formset'] = PatientInlineFormSet(self.request.POST)
        # else:
        ctx['formset'] = self.formset
        #
        # print ('get_context_data')
        # print (ctx)
        return ctx

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form = self.get_form()
    #     formset = self.formset
    #     print ('post:')
    #     print (form)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['formset']
        print(inlines)
        if inlines.is_valid() and form.is_valid():
            # self.formset.save()
            # print(self.inlines)
            self.object = form.save()  # saves Father and Children

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        # ctx = self.get_context_data()
        # inlines = ctx['formset']
        print ('form_invalid')
        # print(inlines)

        return self.render_to_response(self.get_context_data(form=form))


class PatientRecordUpdateView(UpdateView):
    model = Patient
    form_class = PatientUpdateForm
    # fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'records/patient_edit.html'

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(PatientRecordUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['formset'] = PatientInlineFormSet(self.request.POST)
        else:
            ctx['formset'] = PatientInlineFormSet()
        return ctx

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['formset']
        if inlines.is_valid() and form.is_valid():
            # TODO: inlines.save()
            # inlines.save()
            # self.model.objects.filter(pk=self.get_form_kwargs()['instance'].id).update(**form.f003_cleaned_data)
            self.object = form.save()  # saves Father and Children
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

