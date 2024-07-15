from django.db import models

class Parrafo(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50]  # Mostrar los primeros 50 caracteres del párrafo
