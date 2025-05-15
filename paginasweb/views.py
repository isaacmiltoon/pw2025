from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Campus, Curso, TipoSolicitacao, Status, Aluno, Servidor, Solicitacao, Historico


class IndexView(TemplateView):
    template_name = 'paginasweb/index.html'


class SobreView(TemplateView):
    template_name = 'paginasweb/sobre.html'


class CampusCreate(CreateView):
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Campus',
        'botao': 'Cadastrar',
    }
 

class CursoCreate(CreateView):
    model = Curso
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'campus']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Curso',
        'botao': 'Cadastrar',
    }


class TipoSolicitacaoCreate(CreateView):
    model = TipoSolicitacao
    template_name = 'paginasweb/form.html'
    fields = ['descricao', 'prazo_externo', 'prazo_externo_dias', 'prazo_interno', 'prazo_interno_dias']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Tipo de Solicitação',
        'botao': 'Cadastrar',
    }


class StatusCreate(CreateView):
    model = Status
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Status',
        'botao': 'Cadastrar',
    }


class AlunoCreate(CreateView):
    model = Aluno
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'matrícula', 'cpf', 'email', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Aluno',
        'botao': 'Cadastrar',
    }


class ServidorCreate(CreateView):
    model = Servidor
    template_name = 'paginasweb/form.html'
    fields = ['nome', 'siape', 'email']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Servidor',
        'botao': 'Cadastrar',
    }


class SolicitacaoCreate(CreateView):
    model = Solicitacao
    template_name = 'paginasweb/form.html'
    fields = ['solicitado_por', 'curso', 'turma', 'tipo_solicitação', 'justificativa']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Protocolo online da Secretaria',
        'botao': 'Protocolar',
    }


class HistoricoCreate(CreateView):
    model = Historico
    template_name = 'paginasweb/form.html'
    fields = ['solicitacao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastrar Histórico',
        'botao': 'Cadastrar',
    }


##################################################


class CampusUpdate(UpdateView):
    model = Campus
    template_name = 'paginasweb/form.html'
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Atualização de dados do Campus',
        'botao': 'Salvar',
    }


