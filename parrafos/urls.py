from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_texto, name='mostrar_texto'),
    path('anadir/', views.anadir_parrafo, name='anadir_parrafo'),
]
