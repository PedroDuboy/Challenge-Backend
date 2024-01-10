from django.db.models import Count
from django.shortcuts import render
from .models import *
import requests

def inicio(request):
    return render(request, "aplicacion/home.html")

#Joe

def perfil(request):
    joe = Estudiante.objects.get(nombre='Joe')  
    amigos = joe.amigos.all()  
    cursos_amigos = {}
    for amigo in amigos:
        inscripciones_amigo = InscripcionLeccion.objects.filter(estudiante=amigo)
        for inscripcion in inscripciones_amigo:
            curso_nombre = inscripcion.curso.nombre
            if amigo not in cursos_amigos:
                cursos_amigos[amigo] = {'cursos': {curso_nombre: 1}, 'total_cursos': 1}
            else:
                if curso_nombre not in cursos_amigos[amigo]['cursos']:
                    cursos_amigos[amigo]['cursos'][curso_nombre] = 1
                    cursos_amigos[amigo]['total_cursos'] += 1
                else:
                    cursos_amigos[amigo]['cursos'][curso_nombre] += 1
 
    contexto = {'cursos_amigos': cursos_amigos}
    return render(request, "aplicacion/perfil.html", contexto)

def listar_amistades(request):
    joe = Estudiante.objects.get(nombre='Joe')
    amigos = joe.amigos.all()
    contexto = {'amigos': amigos, 'joe': joe}
    return render(request, "aplicacion/listar_amistades.html", contexto)

def listar_lecciones(request):
    joe = Estudiante.objects.get(nombre='Joe')
    lecciones_joe = InscripcionLeccion.objects.filter(estudiante=joe)
    contexto = {'lecciones_joe': lecciones_joe, 'joe': joe}
    return render(request, "aplicacion/listar_lecciones.html", contexto)

#listados

def listar_usuarios(request):
    usuarios = Estudiante.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, "aplicacion/listar_usuarios.html", contexto)

def listar_amistades_usuarios(request):
    usuarios_con_amistades = Estudiante.objects.annotate(num_amistades=Count('amigos'))
    contexto = {'usuarios': usuarios_con_amistades}
    return render(request, "aplicacion/listar_amistades_usuarios.html", contexto)

#API

def open_mateo(request):
    url_api = "https://api.open-meteo.com/v1/dwd-icon?latitude=-34.6131&longitude=-58.3772&current=temperature_2m,relative_humidity_2m,is_day,precipitation,rain,wind_speed_10m&timezone=auto"
    response = requests.get(url_api)
    
    if response.status_code == 200:
        data = response.json()
       
        return render(request, 'aplicacion/clima.html', {'data': data})

  