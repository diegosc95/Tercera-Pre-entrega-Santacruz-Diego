from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Aqui esta las formulas para visualizaciones. 

def ver_estudiantes(request):
    return render(request,"ver_estudiantes.html",)

def ver_curso(request):
    return render(request,"ver_cursos.html",)

def ver_profesores(request):
    return render(request,"ver_profes.html",)

def ver_entregables(request):
    return render(request,"ver_entregas.html",)

def inicio(request):

    return render(request, "inicio.html")

# Aqui esta las formulas para crear info para actualizar nuestra base de datos. 

def crear_curso(request):

    if request.method == "POST": # que sepa que use el boton de enviar
        curso_nuevo = Curso(nombre=request.POST["curso_nombre"],comision =request.POST["curso_comision"])
        curso_nuevo.save()
        return render(request,"inicio.html")
    
    return render(request,"crear_cursos.html")

def crear_entregas(request):
    if request.method == "POST":
        nombre = request.POST["entregable_nombre"]
        fecha_entrega = request.POST["entregable_fecha"]
        entregado = request.POST.get("entregable") == "on"

        entrega_nueva = Entregable(nombre=nombre, fechaEntrega=fecha_entrega, entregado=entregado)
        entrega_nueva.save()
        return render(request, "inicio.html")
    
    return render(request, "crear_entregas.html")

def crear_profesores(request):

    if request.method == "POST": # que sepa que use el boton de enviar
        profe_nuevo = Profesor(nombre=request.POST["profesor_nombre"], apellido=request.POST["profesor_apellido"], email=request.POST["profesor_email"],profesion=request.POST["curso_profesion"])
        profe_nuevo.save()
        return render(request,"inicio.html")
    
    return render(request,"crear_profes.html")    

def crear_estudiante(request):

    if request.method == "POST": # que sepa que use el boton de enviar
        estudiante_nuevo = Estudiantes(nombre=request.POST["estudiante_nombre"], apellido=request.POST["estudiante_apellido"], email=request.POST["estudiante_email"],edad=request.POST["estudiante_edad"])
        estudiante_nuevo.save()
        return render(request,"inicio.html")
    
    return render(request,"crear_estudiantes.html") 

# Aqui esta las formulas para buscar info en nuestra base de datos. 

def buscar_cursos(request):
    mensaje = None
    cursos = None

    if request.GET:
        nombre = request.GET.get("nombre", None)

        if nombre and nombre.strip():  # Verificar que el nombre no esté vacío o solo contenga espacios en blanco
            cursos = Curso.objects.filter(nombre__icontains=nombre)

            if cursos.exists():
                mensaje = f'¡Felicidades, hemos encontrado los siguientes cursos para: {nombre}'
            else:
                mensaje = f'Lo siento, no se encontraron cursos para: {nombre}'
        else:
            mensaje = 'Por favor, ingrese al menos un carácter para realizar la búsqueda.'

    return render(request, "inicio.html", {"mensaje": mensaje, "cursos": cursos})





