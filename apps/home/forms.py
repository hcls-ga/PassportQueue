# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - Hall County Library System
dyoung@hallcountylibrary.org
"""

from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput


#Yes/No Options

YNoptions = (
    (False, "-"),
    (True,"Yes"),
    (False,"No"),
)

YNAoptions = (
    (False, "-"),
    (True,"Yes"),
    (False,"No"),
    (True,"N/A")
)

YNoptionsES = (
    (False, "-"),
    (True,"Si"),
    (False,"No"),
)

YNAoptionsES = (
    (False, "-"),
    (True,"Si"),
    (False,"No"),
    (True,"N/A")
)

def YN_validator(value):
    if value == "No" or value == False or value == "False":
        raise forms.ValidationError("You MUST have the information requested.")
    else:
        print(value)

def YN_validatorES(value):
    if value == "No" or value == False or value == "False":
        raise forms.ValidationError("DEBE tener la información solicitada.")
    else:
        print(value)


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
    finishedApp = forms.TypedChoiceField(
            #label="Before submitting this form please make sure you have already filled out a passport application in BLACK ink",
            choices=YNoptions,
            widget=forms.Select(
                attrs={'class':'form-select'}
            ),
        validators=[YN_validator,]
        )

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
        ),
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
        label="Are both parents present or do you have correct supplemental documentation?",
        choices=YNAoptions,
        widget=forms.Select(
            attrs={'class':'form-select'}
        ),
        validators=[YN_validator,]
    )

    IDtype = forms.ChoiceField(
        widget=forms.RadioSelect(
            
        ),
        choices=(
                (1,"Original Birth certificate"),
                (2,"Certified Copy of Birth Certificate"),
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

class patronRegistrationES(forms.Form):
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
    finishedApp = forms.TypedChoiceField(
            #label="Before submitting this form please make sure you have already filled out a passport application in BLACK ink",
            choices=YNoptionsES,
            widget=forms.Select(
                attrs={'class':'form-select'}
            ),
        validators=[YN_validatorES,]
        )

    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeHolder":"Apellido",
                "class":"form-control"
            }
        )
    )

    phoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeHolder":"Número de teléfono",
                "class":"form-control"
            }
        )
    )

    photosNeeded = forms.TypedChoiceField(
        label="¿Necesita fotos?",
        choices=YNoptionsES,
        widget=forms.Select(
            attrs={'class':'form-select'}
        ),
    )

    numPassports = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeHolder":"Numero de personas que quieren aplicar.",
                "class":"form-control"
            }
        )
    )

    validID = forms.TypedChoiceField(
        label="¿Tiene una identificación válida emitida por el estado?",
        choices=YNoptionsES,

        widget=forms.Select(
            attrs={'class':'form-select'}
        ),
        validators=[YN_validatorES,]
    )

    moneyOrder = forms.TypedChoiceField(
        label="¿Tiene un cheque o Money Order para el Departamento de Estado?",
        choices=YNoptionsES,
        widget=forms.Select(
            attrs={'class':'form-select'}
        ),
        validators=[YN_validatorES,]
    )

    parentApproval = forms.TypedChoiceField(
        label="¿Ambos padres están presentes o tiene la documentación complementaria correcta?",
        choices=YNAoptionsES,
        widget=forms.Select(
            attrs={'class':'form-select'}
        ),
        validators=[YN_validatorES,]
    )

    IDtype = forms.ChoiceField(
        widget=forms.RadioSelect(
            
        ),
        choices=(
                (1,"Acta de nacimiento original"),
                (2,"Copia Certificada del Acta de Nacimiento"),
                (3,"Pasaporte Vencido"),
                (4,"Certificado de naturalización"),
            )
        )

    libraryPayment = forms.TypedChoiceField(
            label="¿Está preparado para pagarle a la biblioteca una tarifa separada de $35/pasaporte (más $15/foto adicional)?",
            choices=YNoptionsES,
            widget=forms.Select(
                attrs={'class':'form-select'}
            ),
        validators=[YN_validatorES,]
        )

class patronModification(forms.Form):
    """
#Notes

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
                "placeHolder":"Last Name",
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

    photoCount = forms.IntegerField(
        label="Number of Photos Taken",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    minorCount = forms.IntegerField(
        label="Number of Minor Passports",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    adultCount = forms.IntegerField(
        label="Number of Adult Passports",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    expeditedCount = forms.IntegerField(
        label="Number of Passport Expedited",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    submitted = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                "class":"form-control datetimepicker-input",
                'data-target': '#datetimepicker1'
            }
        )
    )
    
    started = forms.DateTimeField(
        widget=DateTimePickerInput(
            attrs={
                "class":"form-control datetimepicker-input"
            }
        )
    )

    finished = forms.DateTimeField(
        widget=DatePickerInput(
            attrs={
                "class":"form-control datetimepicker-input"
            }
        )
    )
