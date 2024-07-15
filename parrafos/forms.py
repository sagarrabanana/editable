from django import forms
from .models import Parrafo

class ParrafoForm(forms.ModelForm):
    class Meta:
        model = Parrafo
        fields = ['titulo', 'texto']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título'}),
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe tu párrafo aquí...'}),
        }
