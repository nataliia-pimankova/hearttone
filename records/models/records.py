# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Record(TimeStampedModel):
    """Record Model"""

    class Meta(object):
        verbose_name = u"Record"
        verbose_name_plural = u"Records"

    # status.
    STATUS_CHOICE_NEW = 1
    STATUS_CHOICE_PROCESSING = 2
    STATUS_CHOICE_FINISHED = 3
    STATUS_CHOICES = (
        (STATUS_CHOICE_NEW, u"New"),
        (STATUS_CHOICE_PROCESSING, u"Processing"),
        (STATUS_CHOICE_FINISHED, u"Finished"),
    )

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

    # status = {'new', 'processing', 'finished'}// record processing status
    status = models.IntegerField(
        verbose_name=u"Status",
        choices=STATUS_CHOICES,
        default=1,
    )

    notes = models.CharField(
        max_length=256,
        verbose_name=u"Notes",
        null=True,
        blank=True,
        default=u""
    )

    def __unicode__(self):
        return u"%s %s" % (self.patient, self.path_to_file)
