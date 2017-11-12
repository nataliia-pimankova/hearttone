# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Doctor(TimeStampedModel):
    """Doctor Model"""

    class Meta(object):
        verbose_name = u"Doctor"
        verbose_name_plural = u"Doctors"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"First Name"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Last Name"
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Middle Name",
        default=''
    )

    phone = models.CharField(
        max_length=30,
        verbose_name=u"Phone",
        blank=True,
        null=True,
    )

    hospital = models.ForeignKey(
        'Hospital',
        verbose_name=u'Hospital',
        null=True,
    )

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
