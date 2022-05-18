# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import patronRegistration
from apps.home.models import Patron
import pytz
#def register(CreateView):
    


def index(request):
    context = {'segment': 'index'}
    

    msg = "Test"

    if request.method == 'POST':
        form = patronRegistration(request.POST)
        msg = "Wasn't Valid"
        if form.is_valid():
            lName = form.cleaned_data.get("lastName")
            pNumber = form.cleaned_data.get("phoneNumber")
            photos = form.cleaned_data.get("photosNeeded")
            numPassports = form.cleaned_data.get("numPassports")
            validID = form.cleaned_data.get("validID")
            moneyOrder = form.cleaned_data.get("moneyOrder")
            minorInfo = form.cleaned_data.get("parentApproval")
            IDType = form.cleaned_data.get("IDType")
            libraryPayment = form.cleaned_data.get("libraryPayment")
            msg = lName
            patron = Patron(
                last_name = lName,
                phone_number = pNumber,
                photo_status = photos,
                total_passports = numPassports,
                datetime_submitted = datetime.now(pytz.utc),
                status = "waiting"
            ).save()
    else:
        form = patronRegistration()


    #return render(request, "accounts/login.html")
    #html_template = loader.get_template('home/index.html')
    return render(request,'home/index.html', {"form": form, "msg":msg})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
