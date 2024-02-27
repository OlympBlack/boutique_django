from django.core import validators
from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        widgets = { 
            'nom': forms.TextInput(attrs={'class': 'form-control border-primary'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control border-primary'}),
            #'tag': forms.ChoiceInput(attrs={'class': 'form-control border-primary'}),
        }