from django.urls import path
from .views import IndexView, SobreView
from .views import CampusCreate, CursoCreate, TipoSolicitacaoCreate, StatusCreate, AlunoCreate, ServidorCreate, SolicitacaoCreate, HistoricoCreate

from .views import CampusUpdate

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),  # URL para a página inicial
    path("sobre/", SobreView.as_view(), name="sobre"),

    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),  # URL para criar um novo campus
    path("cadastrar/curso/", CursoCreate.as_view(), name="cadastrar-curso"),  # URL para criar um novo curso
    path("cadastrar/tipo-solicitacao/", TipoSolicitacaoCreate.as_view(), name="cadastrar-tipo-solicitacao"),  # URL para criar um novo tipo de solicitação
    path("cadastrar/status/", StatusCreate.as_view(), name="cadastrar-status"),  # URL para criar um novo status
    path("cadastrar/aluno/", AlunoCreate.as_view(), name="cadastrar-aluno"),  # URL para criar um novo aluno
    path("cadastrar/servidor/", ServidorCreate.as_view(), name="cadastrar-servidor"),  # URL para criar um novo servidor
    path("cadastrar/solicitacao/", SolicitacaoCreate.as_view(), name="cadastrar-solicitacao"),  # URL para criar uma nova solicitação
    path("cadastrar/historico/", HistoricoCreate.as_view(), name="cadastrar-historico"),  # URL para criar um novo histórico

    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),

]
