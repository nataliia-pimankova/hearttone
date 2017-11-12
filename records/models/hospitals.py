# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Hospital(TimeStampedModel):
    """Hospital Model"""

    class Meta(object):
        verbose_name = u"Hospital"
        verbose_name_plural = u"Hospitals"

    hospital_number = models.CharField(
        max_length=10,
        verbose_name=u"Number of Hospital"
    )

    title = models.CharField(
        max_length=100,
        verbose_name=u"Name of Hospital"
    )

    address = models.CharField(
        max_length=256,
        verbose_name=u"Address",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30,
        verbose_name=u"Phone",
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return u"%s %s" % (self.hospital_number, self.title)
