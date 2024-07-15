from django.db import models

class Parrafo(models.Model):
    titulo = models.CharField(max_length=200, default="Título Predeterminado")
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
