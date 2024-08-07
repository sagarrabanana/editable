from django.db import models

class Parrafo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()  # Usar TextField en lugar de CKEditor5Field
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_anchor(self):
        return f"parrafo-{self.pk}"
