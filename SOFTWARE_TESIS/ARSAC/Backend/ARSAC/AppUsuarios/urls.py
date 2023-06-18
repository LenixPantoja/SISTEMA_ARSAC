from django.urls import path
from .views import APIView, AppUser_ApiView_Detail, AppUser_ApiView_List, AppUser_Permiso_ApiView, AppUser_Permiso_ApiView_List, AppUser_Permiso_ApiView_Detail, AppUser_ApiView, AppUser_Periodo_ApiView, AppUser_Periodo_ApiView_List, AppUser_Periodo_ApiView_Detail, AppUser_Horario_ApiView, AppUser_Horario_ApiView_List, AppUser_Horario_ApiView_Detail, AppUser_Materia_ApiView
from AppUsuarios import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    # Crea un token

    path('post/create/', views.create_post, name='creando-post'),
    # Api para obtener un token
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Api para actualizar el toke creado
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # Crea permisos de usuario
    path('v1/permiso/', AppUser_Permiso_ApiView.as_view(), name='crear-permiso'),
    # Responde con una lista de objetos json de permisos
    path('v2/listaPermisos', AppUser_Permiso_ApiView_List.as_view(), name='listar-permisos'),
    # Consulta, editar y eliminar un permiso
    path('v3/permiso/<int:pk>', AppUser_Permiso_ApiView_Detail.as_view(), name='consulta-permisos'),
    # Crear una persona con un usuario

    path('v1/persona', AppUser_ApiView.as_view(), name='crear-persona'),
    # Responde con una lista de objetos json de personas
    path('v2/listaPersonas', AppUser_ApiView_List.as_view(), name='listar-personas'),
    # Consulta, editar y eliminar un permiso
    path('v3/persona/<int:pk>', AppUser_ApiView_Detail.as_view(), name='consulta-personas'),
    # Api para crear periodosAcademicos
    path('v1/periodo', AppUser_Periodo_ApiView.as_view(), name='crear-periodo'),
    # Api que responde con una lista de los periodos
    path('v2/listaPeriodos', AppUser_Periodo_ApiView_List.as_view(), name='listar-permisos'),
    # Api que permite consultar, eliminar un periodo
    path('v3/periodo/<int:pk>', AppUser_Periodo_ApiView_Detail.as_view(), name='consultar-periodos'),
    # Api que permite crear horarios
    path('v1/horario', AppUser_Horario_ApiView.as_view(), name='crear-horario'),
    # Api que responde con una lista de los horarios establecidos
    path('v2/listarHorarios', AppUser_Horario_ApiView_List.as_view(), name='listarHorarios'),
    # Api que permite consultar, editar y eliminar y horario
    path('v3/horario/<int:pk>', AppUser_Horario_ApiView_Detail.as_view(), name='consultar-horarios'),
    # Crea una materia
    path('v1/materia/add/', AppUser_Materia_ApiView.as_view(), name='crear-materia')


]
