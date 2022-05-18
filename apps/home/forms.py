# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Copyright (c) 2022 - Hall County Library System
dyoung@hallcountylibrary.org
"""

from logging import PlaceHolder
from tkinter.ttk import Label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Yes/No Options

YNoptions = (
    (True,"Yes"),
    (False,"No"),
)

def YN_validator(value):
    if value == "No" or value == False:
        raise forms.ValidationError("This Questions MUST be a 'Yes'")


class patronRegistration(forms.Form):
    """
    We will start with the actual form objects then continue onto the DEF functions for validation.
    Basically anytime there is a 'No' value, it will raise an input error. Kind of lame.
    9 Questions
    
    Last Name
    Phone Number
    Photos Needed
    Number of passports
    valid ID
    Money Order for State department
    Minor info
    ID Type
    Library Payment
    """
    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeHolder":"Last Name",
                "class":"form-control"
            }
        )
    )

    phoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeHolder":"Phone Number",
                "class":"form-control"
            }
        )
    )

    photosNeeded = forms.TypedChoiceField(
        label="Do you need photos taken?",
        choices=YNoptions,
            widget=forms.Select(
                attrs={'class':'form-select'}
            )
    )

    numPassports = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeHolder":"Number of people applying for passports",
                "class":"form-control"
            }
        )
    )

    validID = forms.TypedChoiceField(
        label="Do you have a valid stat issued ID?",
        choices=YNoptions,
            widget=forms.Select(
                attrs={'class':'form-select'}
            ),
        validators=[YN_validator,]
    )

    moneyOrder = forms.TypedChoiceField(
        label="Do you have a check or a money order for the State Department?",
        choices=YNoptions,
            widget=forms.Select(
                attrs={'class':'form-select'}
            ),
        validators=[YN_validator,]
    )

    parentApproval = forms.TypedChoiceField(
        label="Are both parents present or do you have correct supplemntal documentation?",
        choices=(
            (True,"Yes"),
            (False, "No"),
            (None,"N/A"),
        ),
            widget=forms.Select(
                attrs={'class':'form-select'}
            )
    )

    IDtype = forms.ChoiceField(
        widget=forms.RadioSelect(
            
        ),
        choices=(
                (1,"Original Birth certificate"),
                (2,"Certified COpy of Birth Certificate"),
                (3,"Expired Passport"),
                (4,"Certificate of Naturalization"),
            )
        )

    libraryPayment = forms.TypedChoiceField(
            label="Are you prepared to pay the library a separate fee of $35/passport (plus additional $15/photo)?",
            choices=YNoptions,
            widget=forms.Select(
                attrs={'class':'form-select'}
            ),
        validators=[YN_validator,]
        )

    #Starting validation functions.
