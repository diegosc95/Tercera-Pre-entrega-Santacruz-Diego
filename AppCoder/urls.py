from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('curso/', crear_curso),
    path('estudiantes/', crear_estudiante),
    path('profesores/', crear_profesores),
    path('entregas/', crear_entregas),
    path('ver_curso/', ver_curso,name="Curso"),
    path('ver_estudiantes/', ver_estudiantes,name="Estudiantes"),
    path('ver_profesores/', ver_profesores,name="Profes"),
    path('ver_entregas/', ver_entregables,name="Entregas"),
     path('', inicio,name="Home"),
]