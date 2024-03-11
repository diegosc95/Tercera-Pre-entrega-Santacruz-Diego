# Tercera-Pre-entrega-Santacruz-Diego
Este proyecto Django, llamado "Registro de Cursos", es una aplicación web desarrollada como parte de mi trabajo práctico. Aquí encontrarás las instrucciones para que puedas ejecutar la aplicación localmente y verla en acción.
El mismo me base en gran medida en lo visto en las clases 19 a la 21, sumandole cosas que fui viendo por internet

## Requisitos previos

- Python instalado (versión sugerida: 3.12.2)
- Pip (instalador de paquetes de Python) instalado
- Git instalado

## Pasos para visualizar la aplicación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2. Instalar las dependencias:

   `pip install -r requirements.txt`

3. Aplicar migraciones:
  `python manage.py migrate`
   `python .\manage.py makemigrations`
  
4.  Iniciar la aplicación:
   `python manage.py runserver`

5. Visitar la aplicación:
   Abre tu navegador y visita http://127.0.0.1:8000/
   El panel de administración en http://127.0.0.1:8000/admin/.
   usuario: diegosc
   Password: diego1234

7. Detener la aplicación:
   En la terminal donde ejecutaste runserver, presiona Ctrl + C para detener el servidor.


# Listado de Elemenos creados

1. Templates
- crear_cursos.html
- crear_entregas.html
- crear_estudiantes.html
- crear_profes.html
- inicio.html
- padre.html
- ver_cursos.html
- ver_entregas.html
- ver_estudiantes.html
- ver_profes.html

2. Modelos
- Estudiantes
- Curso
- Profesor
- Entregable

3. URL http://127.0.0.1:8000/AppCoder/
- curso/
- entregas/
- profesores/
- estudiantes/
- ver_curso/
- ver_entregas/
- ver_profesores/
- ver_estudiantes/
- buscar_cursos/

# Cualquier duda me avisan. Abrazo!

