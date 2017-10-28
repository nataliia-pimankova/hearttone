# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from records import models

# Register your models here.
admin.site.register(models.Patient)
admin.site.register(models.Hospital)
admin.site.register(models.Doctor)
