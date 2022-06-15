# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from types import NoneType
from django.contrib import admin
from django.http import HttpResponse
import csv
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
# Register your models here.
from . import models
from typing import List, Tuple, Any

from django.contrib.admin import SimpleListFilter
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _


class DefaultListFilter(SimpleListFilter):
    """
    I added this in case we wanted to filter anything else
    
    """
    all_value = '_all'

    def default_value(self):
        raise NotImplementedError()

    def queryset(self, request, queryset):
        if self.parameter_name in request.GET and request.GET[self.parameter_name] == self.all_value:
            return queryset

        if self.parameter_name in request.GET:
            return queryset.filter(**{self.parameter_name:request.GET[self.parameter_name]})

        return queryset.filter(**{self.parameter_name:self.default_value()})

    def choices(self, cl):
        yield {
            'selected': self.value() == self.all_value,
            'query_string': cl.get_query_string({self.parameter_name: self.all_value}, []),
            'display': _('All'),
        }
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == force_text(lookup) or (self.value() == None and force_text(self.default_value()) == force_text(lookup)),
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

class StatusFilter(DefaultListFilter):
    title = _('Active ')
    parameter_name = 'active__exact'

    def lookups(self, request, model_admin):
        return ((True,True), (False,False))

    def default_value(self):
        return True

class patronAdmin(admin.ModelAdmin):
    list_display = ('order','last_name','status','datetime_submitted','total_passports','photo_status')
    list_filter = (StatusFilter,'datetime_submitted','status',)
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
    """
    def changelist_view(self, request, extra_context=None):

        referer = request.META.get('HTTP_REFERER', '')

        test = referer.split(request.META['PATH_INFO'])
        
        if test[-1] == '' and not test[-1].startswith('?'):
            

            if not  'active__exact' in request.GET:
        
                q = request.GET.copy()
                q['active__exact'] = '1'
                request.GET = q
                request.META['QUERY_STRING'] = request.GET.urlencode()
        return super(patronAdmin,self).changelist_view(request, extra_context=extra_context)
    """
admin.site.register(models.Patron, patronAdmin)

