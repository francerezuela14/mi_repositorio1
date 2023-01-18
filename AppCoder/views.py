from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Alumno, Profesor

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):

      return render(request, "AppCoder/cursos.html")

def profesores(request):

      return render(request, "AppCoder/profesores.html")


def alumnos(request):

      return render(request, "AppCoder/alumnos.html")

from AppCoder.forms import CursoFormulario, AlumnoFormulario, ProfesoresFormularios

def cursos(request):

      if request.method == "POST":
      
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      
      else:
            miFormulario = CursoFormulario()
            
      return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def alumnos(request):

      if request.method == "POST":
      
            miFormulario = AlumnoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  alumno = Alumno(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  alumno.save()
                  return render(request, "AppCoder/inicio.html")
      
      else:
            miFormulario = AlumnoFormulario()
            
      return render(request, "AppCoder/alumnos.html", {"miFormulario": miFormulario})



def profesores(request):

      if request.method == "POST":
      
            miFormulario = ProfesoresFormularios(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
                  profesor.save()
                  return render(request, "AppCoder/inicio.html")
      
      else:
            miFormulario = ProfesoresFormularios()
            
      return render(request, "AppCoder/profesores.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
      return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

      respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

      
     
