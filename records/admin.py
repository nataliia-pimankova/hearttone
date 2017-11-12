# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Patient, Doctor, Hospital, Record, RecordPart

# Register your models here.
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Record)
admin.site.register(RecordPart)
