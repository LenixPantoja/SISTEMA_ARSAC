from django.contrib import admin
from .models import Persona, Permiso, PeriodoAcademico, Horario, Materia, Curso
# Register your models here.


class PersonasAdmin(admin.ModelAdmin):
    # readonly_fields=('user','fecha_creacion','cedula','fecha_actualizacion')
    search_fields = ('cedula', 'user', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('cedula', 'user', 'fecha_creacion', 'fecha_actualizacion')
    list_display = ('cedula', 'user', 'fecha_creacion', 'fecha_actualizacion')
    ordering = ('fecha_creacion',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


class PermisoAdmin(admin.ModelAdmin):
    readonly_fields = ('tipoDePermiso', 'fecha_creacion_permiso', 'fecha_actualizacion_permiso')
    search_fields = ('tipoDePermiso', 'fecha_creacion_permiso', 'fecha_actualizacion_permiso')
    list_filter = ('tipoDePermiso', 'fecha_creacion_permiso', 'fecha_actualizacion_permiso')
    list_display = ('tipoDePermiso', 'fecha_creacion_permiso', 'fecha_actualizacion_permiso')
    ordering = ('fecha_creacion_permiso',)


class PeriodoAcademicoAdmin(admin.ModelAdmin):
    readonly_fields = ('periodoAcademico', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('periodoAcademico', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('periodoAcademico', 'fecha_creacion', 'fecha_actualizacion')
    list_display = ('periodoAcademico', 'fecha_creacion', 'fecha_actualizacion')
    ordering = ('fecha_creacion',)


class HorarioAdmin(admin.ModelAdmin):
    readonly_fields = ('Jornada', 'horaInicio', 'horaFin', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('Jornada', 'horaInicio', 'horaFin', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('Jornada', 'horaInicio', 'horaFin', 'fecha_creacion', 'fecha_actualizacion')
    list_display = ('Jornada', 'horaInicio', 'horaFin', 'fecha_creacion', 'fecha_actualizacion')
    ordering = ('Jornada',)


class MateriaAdmin(admin.ModelAdmin):
    # readonly_fields = ('nombreMateria','profesor', 'horario','fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombreMateria', 'profesor', 'horario', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('nombreMateria', 'profesor', 'horario', 'fecha_creacion', 'fecha_actualizacion')
    list_display = ('nombreMateria', 'profesor', 'horario', 'fecha_creacion', 'fecha_actualizacion')
    ordering = ('fecha_creacion',)


class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('materia', 'periodoAcademico', 'estudiante', 'participante', 'cantidadEstudiantes', 'fecha_creacion_curso', 'fecha_actualizacion_curso')
    search_fields = ('materia', 'periodoAcademico', 'estudiante', 'participante', 'cantidadEstudiantes', 'fecha_creacion_curso', 'fecha_actualizacion_curso')
    list_filter = ('materia', 'periodoAcademico', 'estudiante', 'participante', 'cantidadEstudiantes', 'fecha_creacion_curso', 'fecha_actualizacion_curso')
    list_display = ('materia', 'periodoAcademico', 'estudiante', 'participante', 'cantidadEstudiantes', 'fecha_creacion_curso', 'fecha_actualizacion_curso')
    ordering = ('fecha_creacion_curso',)


admin.site.register(Persona, PersonasAdmin)
admin.site.register(Permiso, PermisoAdmin)
admin.site.register(PeriodoAcademico)
admin.site.register(Horario)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Curso, CursoAdmin)
