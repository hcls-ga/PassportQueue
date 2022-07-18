# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('patron/add', views.createPatron, name='patron-create'),
    path('patron/<int:id>/change', views.editPatron, name='change'),

    path('reports', views.reports, name='report'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    
]
