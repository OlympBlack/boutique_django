from django.core import validators
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = { 
            'nom': forms.TextInput(attrs={'class': 'form-control border-primary'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control border-primary'}),
            
        }