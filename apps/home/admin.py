# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.http import HttpResponse
import csv
# Register your models here.
from . import models


class patronAdmin(admin.ModelAdmin):
    list_display = ('order','last_name','status','datetime_submitted','total_passports','photo_status')
    list_filter = ('active','datetime_submitted','status')
    actions = ["export_csv"]

    def export_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_csv.short_description = "Export Selected"

admin.site.register(models.Patron, patronAdmin)
