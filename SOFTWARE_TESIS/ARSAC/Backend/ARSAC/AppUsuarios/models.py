from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Django Admin
# USER lenix
# PASS 02062000


class Permiso(models.Model):
    tipoDePermiso = models.CharField(max_length=20)
    fecha_creacion_permiso = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_permiso = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'

    def __str__(self):
        return str(self.tipoDePermiso)


class Persona(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    cedula = models.CharField(max_length=50, verbose_name="Cedula")
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return str(self.cedula)


class PeriodoAcademico(models.Model):
    periodoAcademico = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return str(self.periodoAcademico)


class Horario(models.Model):
    Jornada = models.CharField(max_length=30)
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField()
    fecha_creacion_horarios = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_horarios = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return str(self.Jornada)


class Materia(models.Model):
    nombreMateria = models.CharField(max_length=100)
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return str(self.nombreHorario)


class Curso(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodoAcademico = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Persona, related_name='cursos_estudiante', on_delete=models.CASCADE)
    participante = models.ForeignKey(Persona, related_name='cursos_participante', on_delete=models.CASCADE)
    cantidadEstudiantes = models.IntegerField()
    fecha_creacion_curso = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_curso = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return str(self.nombreHorario)
