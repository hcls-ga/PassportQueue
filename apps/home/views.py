# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

import pytz
from apps.home.models import Patron
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.db.models import Sum
from django.db.models import Max
from .forms import patronModification, patronRegistration, patronRegistrationES

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
            return redirect('sucess')
    else:
        form = patronRegistration()

    return render(request,'home/index.html', {"form": form, "msg":msg})

def index_ex(request):
    context = {'segment': 'index'}
    

    msg = "Test"

    if request.method == 'POST':
        form = patronRegistrationES(request.POST)
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
            return redirect('sucessES')
    else:
        form = patronRegistrationES()

    return render(request,'home/index_es.html', {"form": form, "msg":msg})


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

def createPatron(request):
    form = patronModification
    return render(request, 'home/patron-create.html', {'form':form})

def editPatron(request, id):
    """
    notes
    """
    instance = Patron.objects.get(id=id)
    form = patronModification(instance=instance)
    form.fields['submitted'].widget = DateTimePickerInput()
    return render(request,
                    'home/patron-edit.html',
                    {'form',form}
    )

def reports(request):
    return render(request, 'home/report.html')

"""
This is the page that users will hit after they sucessfully submit the form.
I am hopeing to have a count of the people in front of them.
"""

def sucess(request):
    # Grab the last person in line
    top = Patron.objects.aggregate(Max('order'))['order__max']
    # Sum of Total_Passports for order numbers larger than 0 and less than the person who just submitted the form. 
    count = Patron.objects.filter(order__lt=top, order__gt=0).aggregate(Sum('total_passports'))

    # It took me 2 hours to figure out that {'count',count} should be {'count':count}
    # I could clean this up but I am done.
    return render(request, 'home/sucess.html', {'count':count['total_passports__sum']})
    
def sucessES(request):
    # Grab the last person in line
    top = Patron.objects.aggregate(Max('order'))['order__max']
    # Sum of Total_Passports for order numbers larger than 0 and less than the person who just submitted the form. 
    count = Patron.objects.filter(order__lt=top, order__gt=0).aggregate(Sum('total_passports'))

    # It took me 2 hours to figure out that {'count',count} should be {'count':count}
    # I could clean this up but I am done.
    return render(request, 'home/sucessES.html', {'count':count['total_passports__sum']})