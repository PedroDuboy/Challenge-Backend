from django.contrib import admin
from .models import *

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'cursos_list', 'amigos_list',)

    def cursos_list(self, obj):
        return ", ".join([curso.nombre for curso in obj.lecciones.all()])
    
    cursos_list.short_description = 'Cursos'

    def amigos_list(self, obj):
        return ", ".join([amigo.nombre for amigo in obj.amigos.all()])
    
    amigos_list.short_description = 'Amigos'

admin.site.register(Curso)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(InscripcionLeccion)