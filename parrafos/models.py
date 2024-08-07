from django.db import models

class Parrafo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()  # Quill content will be stored as HTML
    autor = models.CharField(max_length=100, blank=True, null=True)  # Añadir campo autor
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_anchor(self):
        return f"parrafo-{self.pk}"
