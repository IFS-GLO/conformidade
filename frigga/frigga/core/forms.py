from django import forms

from .models import *


class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }


class SpecieForm(forms.ModelForm):
    class Meta:
        model = Specie
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }
