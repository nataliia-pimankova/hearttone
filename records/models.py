# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Patient(TimeStampedModel):
    """Patient Model"""

    class Meta(object):
        verbose_name = u"Patient"
        verbose_name_plural = u"Patients"

    # стать хворого.
    GENDER_CHOICE_MALE = 1
    GENDER_CHOICE_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_CHOICE_MALE, "чоловіча"),
        (GENDER_CHOICE_FEMALE, "жіноча"),
    )

    number_history = models.CharField(
        max_length=10,
        verbose_name=u"Number of History",
    )

    date_time = models.DateTimeField(
        verbose_name=u"Date and Time",
    )

    gender = models.IntegerField(
        verbose_name="Стать",
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

    path_to_file = models.ImageField(
        blank=True,
        verbose_name=u"Photo",
        null=True
    )

    notes = models.TextField(
        verbose_name="Нотатки",
        blank=True,
        null=True,
    )
