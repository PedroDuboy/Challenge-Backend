from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    lecciones = models.ManyToManyField(Curso, related_name='estudiantes')
    amigos = models.ManyToManyField('self', blank=True) 

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    def cantidad_lecciones(self):
        return self.lecciones.count()

class InscripcionLeccion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} - {self.curso} - {self.fecha_inscripcion}"