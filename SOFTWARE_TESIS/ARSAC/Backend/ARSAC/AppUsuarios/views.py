__author__ = "Lenix Pantoja"
__copyright__ = "Copyright 2023, Arsac"
__credits__ = ["Lenix Pantoja"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Lenix Pantoja"
__email__ = "aldair.pantoja.velasquez@gmail.com"
__status__ = "Developer"


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.hashers import make_password
from .serializers import UsuariosSerializers, PersonasSerializers, PermisosSerializers, PeriodoAcademicoSerializers, HorariosSerializers, MateriasSerializers, CursosSerializers
from .models import Persona, Permiso, PeriodoAcademico, Horario, Materia, Curso
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets

# Librerias para JWT

from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes


# Create your views here.


""" Funcion que permite saber si el JWT fue aceptado"""


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_post(request):
    return JsonResponse({'msg': 'todo funcionando'})


"""@Class AppUser_ApiView y el método POST que permitirá guardar registros en la base de datos"""


class AppUser_ApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = UsuariosSerializers(data=request.data)
        try:
            if serializer.is_valid():
                dat = request.data
                user = User(
                    username=str(dat["username"]),
                    password=make_password(str(dat["password"]), salt=None, hasher='default')
                )
                dataPersona = dat["persona"]
                user.save()
                print(user)
                persona = Persona(
                    user=user,
                    cedula=dataPersona["cedula"],
                    fecha_nacimiento=dataPersona["fecha_nacimiento"],
                    direccion=dataPersona["direccion"],
                    telefono=dataPersona["telefono"],
                )
                persona.save()
                print(dat)

                return JsonResponse({'msg': 'todo funcionando'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""@Class AppUser_ApiView_List clase responderá a la petición GET que traera el listado de nuestros usuarios"""


class AppUser_ApiView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        usuarios = User.objects.all()
        serializer = UsuariosSerializers(usuarios, many=True)
        return Response(serializer.data)


"""@Class AppUsuarios_APYView nos permitira hacer métodos referentes a personas métodos para consultar una sola persona, editar o eliminar una persona con un id determinado o una primary key"""


class AppUser_ApiView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonasSerializers(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonasSerializers(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" CREANDO APIS PARA PERMISOS DE USUARIOS """
"""@Class AppUser_Permiso_ApiView y el método POST que permitirá guardar registros en la base de datos."""


class AppUser_Permiso_ApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = PermisosSerializers(data=request.data)
        if serializer.is_valid():
            dataPermisos = request.data
            permiso = Permiso(
                tipoDePermiso=dataPermisos['tipoDePermiso']
            )
            permiso.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'msg': 'todo funcionando'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""@Class AppUser_Permiso_ApiView_List clase responderá a la petición GET que traera el listado de nuestros permisos"""


class AppUser_Permiso_ApiView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):
        permisos = Permiso.objects.all()
        serializer = PermisosSerializers(permisos, many=True)
        return Response(serializer.data)


"""@Class AppUser_Permiso_ApiView_Detail nos permitira hacer métodos referentes a nuestros permisos métodos para consultar un solo permiso, editar o eliminar un permiso con un id determinado o una primary key"""


class AppUser_Permiso_ApiView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Permiso.objects.get(pk=pk)
        except Permiso.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        permiso = self.get_object(pk)
        serializer = PermisosSerializers(permiso)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        permiso = self.get_object(pk)
        serializer = PermisosSerializers(permiso, data=request.data)  # Se pasa `request.data` como el argumento `data`
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permiso = self.get_object(pk)
        permiso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""@Class AppUser_ApiView y el método POST que permitirá guardar registros de periodos académicos en la base de datos."""


class AppUser_Periodo_ApiView(APIView):
    def post(self, request, format=None):
        serializer = PeriodoAcademicoSerializers(data=request.data)
        if serializer.is_valid():
            dataPeriodo = request.data
            periodo = PeriodoAcademico(
                periodoAcademico=dataPeriodo['periodoAcademico']
            )
            periodo.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'msg': 'todo funcionando'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""@Class AppUser_Permiso_ApiView_List clase responderá a la petición GET que traera el listado de los periodos"""


class AppUser_Periodo_ApiView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):

        periodos = PeriodoAcademico.objects.all()
        # Probar si esto funciona JJAJAJ
        serializer = PeriodoAcademicoSerializers(periodos, many=True)
        return Response(serializer.data)


"""@Class AppUser_Permiso_ApiView_Detail nos permitira hacer métodos referentes a nuestros periodos métodos para consultar un solo periodo, editar o eliminar un periodo con un id determinado o una primary key"""


class AppUser_Periodo_ApiView_Detail(APIView):

    def get_object(self, pk):
        try:
            return PeriodoAcademico.objects.get(pk=pk)
        except PeriodoAcademico.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        periodo = self.get_object(pk)
        serializer = PeriodoAcademicoSerializers(periodo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        periodo = self.get_object(pk)
        serializer = PeriodoAcademicoSerializers(periodo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        periodo = self.get_object(pk)
        periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""@Class AppUser_ApiView y el método POST que permitirá guardar registros de horarios en la base de datos."""


class AppUser_Horario_ApiView(APIView):
    def post(self, request, format=None):
        serializer = HorariosSerializers(data=request.data)
        if serializer.is_valid():

            dataHorario = request.data
            horario = Horario(
                Jornada=dataHorario['Jornada'],
                horaInicio=dataHorario['horaInicio'],
                horaFin=dataHorario['horaFin']
            )
            horario.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'msg': 'todo funcionando'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""@Class AppUser_Horario_ApiView_List clase responderá a la petición GET que traera el listado de los Horarios"""


class AppUser_Horario_ApiView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):

        horarios = Horario.objects.all()
        # Probar si esto funciona JJAJAJ
        serializer = HorariosSerializers(horarios, many=True)
        return Response(serializer.data)


"""@Class AppUser_Horario_ApiView_Detail nos permitira hacer métodos referentes a nuestros horarios métodos para consultar un solo horario, editar o eliminar un horario con un id determinado o una primary key"""


class AppUser_Horario_ApiView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Horario.objects.get(pk=pk)
        except Horario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        horario = self.get_object(pk)
        serializer = HorariosSerializers(horario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        horario = self.get_object(pk)
        serializer = HorariosSerializers(horario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        horario = self.get_object(pk)
        horario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""@Class AppUser_ApiView y el método POST que permitirá guardar registros de Materias en la base de datos."""


class AppUser_Materia_ApiView(APIView):
    def post(self, request, format=None):
        serializer = MateriasSerializers(data=request.data)
        if serializer.is_valid():

            dataMateria = request.data
            PKprofesor = User.objects.get(id=dataMateria['profesor'])
            PKhorario = Horario.objects.get(id=dataMateria['horario'])
            print("codProfesor", PKprofesor)
            print("codHorario", PKhorario)
            materia = Materia(
                nombreMateria=dataMateria['nombreMateria'],
                profesor=PKprofesor,
                horario=PKhorario
            )
            materia.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({'msg': 'todo funcionando'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)