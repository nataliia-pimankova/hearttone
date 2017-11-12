# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class RecordPart(TimeStampedModel):
    """Part of Record Model"""

    class Meta(object):
        verbose_name = u"Part of Record"
        verbose_name_plural = u"Parts of Records"

    record = models.ForeignKey(
        'Record',
        verbose_name=u'Record'
    )

    start_time = models.CharField(
        max_length=30,
        verbose_name=u"Start Time",
    )

    end_time = models.CharField(
        max_length=30,
        verbose_name=u"End Time",
    )

    number = models.PositiveSmallIntegerField(
        verbose_name=u"Number of Part"
    )

    def __unicode__(self):
        return u"%s: %s - %s" % (self.record.patient, self.start_time, self.end_time)
