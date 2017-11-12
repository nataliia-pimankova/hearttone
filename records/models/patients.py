# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Patient(TimeStampedModel):
    """Patient Model"""

    class Meta(object):
        verbose_name = u"Patient"
        verbose_name_plural = u"Patients"

    # gender.
    GENDER_CHOICE_MALE = 1
    GENDER_CHOICE_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_CHOICE_MALE, u"male"),
        (GENDER_CHOICE_FEMALE, u"female"),
    )

    history_number = models.CharField(
        max_length=10,
        verbose_name=u"Number of History",
    )

    date_time = models.DateTimeField(
        verbose_name=u"Date and Time",
    )

    gender = models.IntegerField(
        verbose_name=u"Gender",
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )

    weight = models.CharField(
        max_length=20,
        verbose_name=u"Weight"
    )

    length = models.CharField(
        max_length=20,
        verbose_name=u"Length"
    )

    doctor = models.ForeignKey(
        'Doctor',
        verbose_name=u'Doctor',
        null=True,
    )

    hospital = models.ForeignKey(
        'Hospital',
        verbose_name=u'Hospital',
        null=True,
    )

    comment = models.TextField(
        verbose_name=u"Comment",
        blank=True,
        null=True,
    )

    def __str__(self):
        return u'%s' % self.history_number
