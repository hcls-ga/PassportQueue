# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import django
from sqlalchemy import false, true
from datetime import datetime
import pytz
# Create your models here.

class Patron(models.Model):
    id=models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    photo_count = models.IntegerField(default=0)
    minor_passport_count = models.IntegerField(default=0)
    adult_passport_count = models.IntegerField(default=0)
    expidited_passport_count = models.IntegerField(default=0)
    total_passports = models.IntegerField(default=1)
    datetime_submitted = models.DateTimeField(default=django.utils.timezone.now)
    datetime_started = models.DateTimeField(null=true, blank=true)
    datetime_finished = models.DateTimeField(null=true, blank=true)
    agent = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name="patron", default=1)
    status = models.TextField(
        choices = (
            ("waiting","Waiting"),
            ("in_progress","In Progress"),
            ("executed","Executed"),
            ("cancelled","Cancelled"),
            ("coming_back","Coming Back"),
        ),
    )
    active = models.BooleanField(default=true)
    order = models.IntegerField(default=0)

    @property
    def getActive(self):
        if self.status == "executed" or self.status == "cancelled":
            return False
        else:
            return True

    @property
    def getOrder(self):
        order = 1
        active = Patron.objects.filter(active=True).order_by('datetime_submitted')
        curOrder = self.order
        for i in active:
            if i.datetime_submitted < self.datetime_submitted:
                order = order + 1
            elif i.datetime_submitted > self.datetime_submitted and i.order > 0 and self.getActive:
                curOrder = curOrder + 1
                Patron.objects.filter(id=i.id).update(order = curOrder)
            elif i.datetime_submitted > self.datetime_submitted and i.order > 2 and self.getActive == False:
                curOrder = curOrder - 1
                Patron.objects.filter(id=i.id).update(order = curOrder)
        if not self.getActive:
            order = -1
        return order
    
    def save(self, *args, **kwargs):
        self.active = self.getActive
        self.order = self.getOrder
        super(Patron, self).save(*args, **kwargs)


class Meta():
    ordering = ['-order','date_submitted']