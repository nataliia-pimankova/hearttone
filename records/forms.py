from django.forms import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('save_button', u'Save', css_class='btn btn-primary'))
        self.helper.add_input(Submit('cancel_button', u'Cancel', css_class='btn btn-link'))


class RecordUpdateForm(RecordCreateForm):
    def __init__(self, *args, **kwargs):
        super(RecordUpdateForm, self).__init__(*args, **kwargs)
        self.form_action = reverse('record_edit',
                                   kwargs={'pk': kwargs['instance'].id})
        self.headline = u'Edit Record'


