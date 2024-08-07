from django import forms
from .models import Parrafo
from bs4 import BeautifulSoup
import base64
from io import BytesIO
from PIL import Image

class ParrafoForm(forms.ModelForm):
    class Meta:
        model = Parrafo
        fields = ['titulo', 'texto']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título'}),
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe tu párrafo aquí...'}),
        }

    def clean_texto(self):
        texto = self.cleaned_data.get('texto')
        soup = BeautifulSoup(texto, 'html.parser')
        for img in soup.find_all('img'):
            if 'data:image' in img['src']:  # Check if image is base64 encoded
                base64_str = img['src'].split(',')[1]
                decoded_img = base64.b64decode(base64_str)
                img_io = BytesIO(decoded_img)
                if img_io.getbuffer().nbytes > 2 * 1024 * 1024:  # 2MB
                    raise forms.ValidationError('El tamaño de la imagen no debe exceder los 2MB.')
        return texto
