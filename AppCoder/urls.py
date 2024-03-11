from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('curso/', crear_curso,name="Curso"),
    path('entregas/', crear_entregas,name="Entregas"),
    path('profesores/', crear_profesores,name="Profes"),
    path('estudiantes/', crear_estudiante,name="Estudiantes"),
    path('ver_curso/', ver_curso),
    path('ver_entregas/', ver_entregables),
    path('ver_profesores/', ver_profesores),
    path('ver_estudiantes/', ver_estudiantes),
    path('buscar_cursos/', buscar_cursos),
    path('', inicio,name="Home"),
]