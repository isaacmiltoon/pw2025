from django.urls import path
from .views import (
    index, sobre,
    EspecialidadeCreate, EspecialidadeList,
    MedicoCreate, MedicoList,
    PacienteCreate, PacienteList,
    ConsultaCreate, ConsultaList,
    editar_especialidade, excluir_especialidade
)

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('especialidade/cadastrar/', EspecialidadeCreate.as_view(), name='cadastrar-especialidade'),
    path('especialidade/listar/', EspecialidadeList.as_view(), name='listar-especialidade'),
    path('medico/cadastrar/', MedicoCreate.as_view(), name='cadastrar-medico'),
    path('medico/listar/', MedicoList.as_view(), name='listar-medico'),
    path('paciente/cadastrar/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('paciente/listar/', PacienteList.as_view(), name='listar-paciente'),
    path('consulta/cadastrar/', ConsultaCreate.as_view(), name='cadastrar-consulta'),
    path('consulta/listar/', ConsultaList.as_view(), name='listar-consulta'),
    path('editar-especialidade/<int:id>/', editar_especialidade, name='editar-especialidade'),
    path('excluir-especialidade/<int:pk>/', excluir_especialidade, name='excluir-especialidade'),
]
