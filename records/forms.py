from django.forms import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Field, Submit

from .models import Patient


class RecordCreateForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(RecordCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
    #
        # set form tag attributes
        self.form_action = reverse('record_add',
                     kwargs={})
        self.headline = u'Add Record'
    #
    #     # self.helper.form_tag = True
        self.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
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
            Field('path_to_file', wrapper_class='row'),
            Field('comment', wrapper_class='row'),

            ButtonHolder(
                Submit('save_button', u'Save', css_class='btn btn-primary'),
                Submit('cancel_button', u'Cancel', css_class='btn btn-link'),
                # css_class='row offset-sm-4'
            )
        )

        self.helper.add_layout(layout)

        # form buttons

        # self.helper.add_input(Submit('save_button', u'Save', css_class='btn btn-primary'))
        # self.helper.add_input(Submit('cancel_button', u'Cancel', css_class='btn btn-link'))


class RecordUpdateForm(RecordCreateForm):
    def __init__(self, *args, **kwargs):
        super(RecordUpdateForm, self).__init__(*args, **kwargs)
        self.form_action = reverse('record_edit',
                                   kwargs={'pk': kwargs['instance'].id})
        self.headline = u'Edit Record'


