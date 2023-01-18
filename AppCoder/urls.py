from django.urls import path

from AppCoder import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('alumnos', views.alumnos, name="Alumnos"),
    #path('cursoFormulario', views.cursosformularios, name="CursoFormulario"),
    path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar)
]
