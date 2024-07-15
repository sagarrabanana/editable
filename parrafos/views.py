from django.shortcuts import render, redirect
from .models import Parrafo
from .forms import ParrafoForm

def mostrar_texto(request):
    parrafos = Parrafo.objects.all().order_by('fecha_creacion')
    return render(request, 'parrafos/mostrar_texto.html', {'parrafos': parrafos})

def anadir_parrafo(request):
    if request.method == 'POST':
        form = ParrafoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_texto')
    else:
        form = ParrafoForm()
    return render(request, 'parrafos/anadir_parrafo.html', {'form': form})
