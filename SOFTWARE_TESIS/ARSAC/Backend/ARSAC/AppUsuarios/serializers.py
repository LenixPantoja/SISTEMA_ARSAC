from rest_framework import serializers
from .models import Persona, Permiso, PeriodoAcademico, Horario, Materia, Curso
from django.contrib.auth.models import User


""" Clase serializable de Personas """


class PersonasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


""" Clase serializable de usuarios """


class UsuariosSerializers(serializers.ModelSerializer):
    persona = PersonasSerializers()

    class Meta:
        model = User
        fields = '__all__'


""" Clase serializable de permisos """


class PermisosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'


""" Clase serializable de Peridodos academicos """


class PeriodoAcademicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = '__all__'


class HorariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'


class MateriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'


class CursosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
