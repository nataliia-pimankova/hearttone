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

    # status.
    STATUS_CHOICE_NEW = 1
    STATUS_CHOICE_THENORM = 2
    STATUS_CHOICE_NOTTHENORM = 3
    STATUS_CHOICE_SOMETHINGSTRANGE = 4
    STATUS_CHOICES = (
        (STATUS_CHOICE_NEW, u"New"),
        (STATUS_CHOICE_THENORM, u"The Norm"),
        (STATUS_CHOICE_NOTTHENORM, u"Not The Norm"),
        (STATUS_CHOICE_SOMETHINGSTRANGE, u"Something Strange"),
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

    # status = {'new', 'norm', 'not norm', 'something strange'}// patient status
    status = models.IntegerField(
        verbose_name=u"Status",
        choices=STATUS_CHOICES,
        default=1,
    )

    ultrasound_findings = models.ImageField(
        blank=True,
        verbose_name=u"Ultrasound Findings",
        upload_to='ultrasound',
        null=True
    )

    # congenital heart defects (CHD)
    congenital_heart_defects = models.BooleanField(
        verbose_name=u'Congenital Heart Defects (CHD)',
        default=False,
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

    mobile_phone = models.CharField(
        max_length=50,
        verbose_name=u"Parent's Phone",
        null=True,
    )

    email = models.EmailField(
        max_length=50,
        verbose_name=u"Parent's Email",
        null=True,
    )

    comment = models.TextField(
        verbose_name=u"Comment",
        blank=True,
        null=True,
    )

    def __str__(self):
        return u'%s' % self.history_number
