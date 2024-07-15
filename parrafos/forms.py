from django import forms
from .models import Parrafo

class ParrafoForm(forms.ModelForm):
    class Meta:
        model = Parrafo
        fields = ['texto']
