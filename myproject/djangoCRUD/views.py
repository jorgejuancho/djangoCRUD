from django.shortcuts import render, redirect
from .models import Registros


# Create your views here.
def home(request):
    registros = Registros.objects.all()
    return render(request, 'index.html', {'Registros': registros})


def agregar(request):
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    correo = request.POST['correo']
    materia = request.POST['materia']

    registro = Registros.objects.create(
        nombre = nombre,
        apellidos =apellidos,
        correo =correo,
        materia = materia
    )
    return redirect('/')

def borrar(request, id):
    registro = Registros.objects.get(id=id)
    registro.delete()
    return redirect('/')
   
def editar (request, id):
    registro = Registros.objects.get(id=id)
    return render(request, 'editar.html', {"registro":registro})

def actualizar (request, id):
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    correo = request.POST['correo']
    materia = request.POST['materia']
    
    registro = Registros.objects.get(id=id)
    registro.nombre = nombre
    registro.apellidos =apellidos
    registro.correo =correo
    registro.materia = materia
                
    registro.save()
    return redirect('/')
