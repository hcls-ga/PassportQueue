# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from random import choices
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone
import django
from django.db.models import Q
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

class Patron(models.Model):
    id=models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(null=True,max_length=200)
    photo_status = models.BooleanField(default=False)
    photo_count = models.IntegerField(default=0)
    minor_passport_count = models.IntegerField(default=0)
    adult_passport_count = models.IntegerField(default=0)
    expidited_passport_count = models.IntegerField(default=0)
    total_passports = models.IntegerField(default=1)
    datetime_submitted = models.DateTimeField(default=django.utils.timezone.now)
    datetime_started = models.DateTimeField(null=True, blank=True)
    datetime_finished = models.DateTimeField(null=True, blank=True)
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
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    @classmethod
    def from_db(cls, db, field_names, values):

        instance = super().from_db(db, field_names, values)
        instance._loaded_values = dict(zip(field_names,values))
        return instance

    @property
    def getActive(self):
        if self.status == "executed" or self.status == "cancelled":
            return False
        else:
            return True

    @property
    def getOrder(self):
        active = Patron.objects.filter(active=True).filter(~Q(id=self.id)).order_by('datetime_submitted')
        curOrder = 1
        nextOrder = 1
        
        for i in active:
            #if it's added and it's time is greater than i's time add one to it's order number
            if i.datetime_submitted < self.datetime_submitted:
                curOrder = curOrder + 1
                Patron.objects.filter(id=i.id).update(order = nextOrder)
                nextOrder = nextOrder + 1
            #if it's added and it's time is less than i's time add on to the next order variable and assign it
            elif i.datetime_submitted > self.datetime_submitted and i.order > 0 and self.getActive and i.active:
                nextOrder = nextOrder + 1
                Patron.objects.filter(id=i.id).update(order = nextOrder)
            #if it's removed and it's time is less than i's sub one to the next order and assign
            elif i.datetime_submitted > self.datetime_submitted and self.getActive == False:
                Patron.objects.filter(id=i.id).update(order = nextOrder)
                nextOrder = nextOrder + 1
        #This is here just in case I missed something or a photon flips a bit. Probs can remove it but it ain't broke.
        if not self.getActive:
            curOrder = -1
        if curOrder == -1 and self.getActive:
            self.order = 0
            curOrder = self.getOrder
        return curOrder

        
    def save(self, *args, **kwargs):
        self.active = self.getActive
        self.order = self.getOrder
        #This was a test and I am not sure if I can remove it but it's currently working so...
        if not self._state.adding:
            newDate = self.datetime_submitted
            if self._loaded_values['datetime_submitted'] != self.datetime_submitted and self._loaded_values['datetime_submitted'] != None:
                self._loaded_values['datetime_submitted'] = self.datetime_submitted
                self.save
                
        super(Patron, self).save(*args, **kwargs)

    def countActive(self):
        # I made this because it wasn't working as in the views.py
        # I was passing a set instead of a dict
        # I leave this here as a monument to my stupidity
        active = Patron.objects.filter(active=True)
        count = active.count

        return count

class Question(models.Model):

    id = models

    def save(self, *args, **kwargs):
        super(Patron, self).save(*args, **kwargs)

class Meta():
    ordering = ['-order','date_submitted']

