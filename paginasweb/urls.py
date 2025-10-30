from django.urls import path
from django.urls import reverse_lazy
from .views import CadastroUsuarioView

from .views import (
    index, sobre,
    EspecialidadeCreate, EspecialidadeList, EspecialidadeUpdate, EspecialidadeDelete,
    MedicoCreate, MedicoList, MedicoUpdate, MedicoDelete,
    PacienteCreate, PacienteList, PacienteUpdate, PacienteDelete,
    ConsultaCreate, ConsultaList, ConsultaUpdate, ConsultaDelete,
)

from django.contrib.auth import views as auth_views


urlpatterns = [

    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),    
    path("autenticar/" , auth_views.LoginView.as_view(
        template_name= 'paginasweb/forms.html',
        extra_context = {
            'titulo' : "Autenticação",
            'botao' : 'Entrar' ,
        }
        ), name="autenticar"),

    path("senha/" , auth_views.PasswordChangeView.as_view(
        template_name= 'paginasweb/forms.html',
        success_url= reverse_lazy('index'),
        extra_context = {
            'titulo' : "Atualizar senha",
            'botao' : 'Salvar' ,
        }
        ), name="senha"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('especialidade/cadastrar/', EspecialidadeCreate.as_view(), name='cadastrar-especialidade'),
    path('especialidade/listar/', EspecialidadeList.as_view(), name='listar-especialidade'),
    path('especialidade/editar/<int:pk>/', EspecialidadeUpdate.as_view(), name='editar-especialidade'),
    path('especialidade/excluir/<int:pk>/', EspecialidadeDelete.as_view(), name='excluir-especialidade'),
    path('medico/cadastrar/', MedicoCreate.as_view(), name='cadastrar-medico'),
    path('medico/listar/', MedicoList.as_view(), name='listar-medico'),
    path('paciente/cadastrar/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('paciente/listar/', PacienteList.as_view(), name='listar-paciente'),
    path('paciente/editar/<int:pk>/', PacienteUpdate.as_view(), name='editar-paciente'),
    path('paciente/excluir/<int:pk>/', PacienteDelete.as_view(), name='excluir-paciente'),
    path('consulta/cadastrar/', ConsultaCreate.as_view(), name='cadastrar-consulta'),
    path('consulta/listar/', ConsultaList.as_view(), name='listar-consulta'),
    path('consulta/editar/<int:pk>/', ConsultaUpdate.as_view(), name='editar-consulta'),
    path('consulta/excluir/<int:pk>/', ConsultaDelete.as_view(), name='excluir-consulta'),
    path('medico/editar/<int:pk>/', MedicoUpdate.as_view(), name='editar-medico'),
    path('medico/excluir/<int:pk>/', MedicoDelete.as_view(), name='excluir-medico'),
]
