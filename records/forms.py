from django.forms import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Field, Submit, Fieldset
from django.forms.models import formset_factory, inlineformset_factory

from .models import Patient, Record


class PatientForm(ModelForm):
    """Patient form"""

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.labels_uppercase = True

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 col-form-label'
        self.helper.field_class = 'col-sm-8'
        layout = Layout(
            Field('history_number', wrapper_class='row'),
            Field('hospital', wrapper_class='row'),
            Field('doctor', wrapper_class='row'),
            Field('date_time', wrapper_class='row'),
            Field('gender', wrapper_class='row'),
            Field('weight', wrapper_class='row'),
            Field('length', wrapper_class='row'),
            Field('ultrasound_findings', wrapper_class='row'),
            Field('congenital_heart_defects', wrapper_class='row'),
            Field('mobile_phone', wrapper_class='row'),
            Field('email', wrapper_class='row'),
            # TODO: status of patient - readonly
            Field('status', wrapper_class='row', css_class='form-control-plaintext', readonly='readonly'),
            Field('comment', wrapper_class='row'),

        )

        self.helper.add_layout(layout)
        super(PatientForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Patient
        fields = ('__all__')


class RecordInlineForm(ModelForm):
    """Record form"""

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.labels_uppercase = True

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 col-form-label'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            Field('path_to_file', wrapper_class='row'),
            # TODO: status o record - readonly
            Field('status', wrapper_class='row'),
            Field('notes', wrapper_class='row'),
        )
        super(RecordInlineForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ['path_to_file', 'status', 'notes']
        model = Record


class PatientCreateForm(ModelForm):

    class Meta:
        model = Patient
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(PatientCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
    #
        # set form tag attributes
        self.form_action = reverse('patient_add',
                     kwargs={})
        self.headline = u'Add Patient'
    #
        self.helper.form_tag = False
        self.form_method = 'POST'
        self.helper.labels_uppercase = True

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 col-form-label'
        self.helper.field_class = 'col-sm-8'

        layout = Layout(
            Field('history_number', wrapper_class='row'),
            Field('hospital', wrapper_class='row'),
            Field('doctor', wrapper_class='row'),
            Field('date_time', wrapper_class='row'),
            Field('gender', wrapper_class='row'),
            Field('weight', wrapper_class='row'),
            Field('length', wrapper_class='row'),
            Field('comment', wrapper_class='row'),

        )
        self.helper.add_layout(layout)


class PatientUpdateForm(PatientCreateForm):
    def __init__(self, *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        self.form_action = reverse('patient_edit',
                                   kwargs={'pk': kwargs['instance'].id})
        self.headline = u'Edit Patient'


