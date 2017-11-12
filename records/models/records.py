# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Record(TimeStampedModel):
    """Record Model"""

    class Meta(object):
        verbose_name = u"Record"
        verbose_name_plural = u"Records"

    patient = models.ForeignKey(
        'Patient',
        verbose_name=u'Patient'
    )

    path_to_file = models.FileField(
        blank=True,
        verbose_name=u"Record",
        upload_to='',
        null=True
    )

    # status_ = {'new', 'processing', 'finished'}// record processing status


    notes = models.CharField(
        max_length=256,
        verbose_name=u"Notes",
        null=True,
        default=u""
    )

    def __unicode__(self):
        return u"%s %s" % (self.patient, self.path_to_file)
