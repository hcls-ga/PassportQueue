# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from . import models

class patronAdmin(admin.ModelAdmin):
    list_display = ('order','last_name','status','datetime_submitted','total_passports','photo_status')
    list_filter = ('active',)

admin.site.register(models.Patron, patronAdmin)
