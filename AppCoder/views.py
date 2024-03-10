from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.

def ver_estudiantes(request):
    return render(request,"ver_estudiantes.html",)

def ver_curso(request):
    return render(request,"ver_cursos.html",)

def ver_profesor(request):
    return render(request,"ver_profes.html",)

def ver_entregable(request):
    return render(request,"ver_entregas.html",)


def inicio(request):

    return render(request, "inicio.html")

def ver_estudiantes(request):

    return render(request, "ver_estudiantes.html")

def ver_cursos(request):

    return render(request, "ver_cursos.html")

def ver_profesores(request):

    return render(request, "ver_profes.html")

def ver_entregables(request):

    return render(request, "ver_entregas.html")

def crear_curso(request):

    curso_1 = Curso(nombre="SQL", comision=50211)
    
    curso_1.save()
     
    return HttpResponse("Info creada")

def crear_estudiante(request):

    est_1 = Estudiantes(nombre="Diego", apellido="Santacruz", email="die@h.com",edad=29 )
    est_2 = Estudiantes(nombre="Elias", apellido="Jara", email="eli@h.com",edad=19 )

    est_1.save()
    est_2.save()

    info = {"nombre1":est_1.nombre,"nombre2":est_2.nombre,}

    return render(request,"crear_estudiantes.html",info)

def crear_profesores(request):

    profe_1 = Profesor(nombre="Juan", apellido="Perez", email="jua@h.com",profesion="Abogado")
    
    profe_1.save()
    
    return render(request,"crear_profes.html")

def crear_entregas(request):

    ent_1 = Entregable(nombre="Diego",fechaentrega="2024-02-01",entregado=1)

    ent_1.save()
    
    return render(request,"crear_entregas.html")