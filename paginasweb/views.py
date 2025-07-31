from django.views.generic import CreateView, ListView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Especialidade, Medico, Paciente, Consulta
from .forms import EspecialidadeForm  

from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    return render(request, 'paginasweb/index.html')

def sobre(request):
    return render(request, 'paginasweb/sobre.html')
def editar_especialidade(request, id):
    especialidade = get_object_or_404(Especialidade, id=id)

    if request.method == 'POST':
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            return redirect('listar-especialidade') 
    else:
        form = EspecialidadeForm(instance=especialidade)

    return render(request, 'paginasweb/especialidade.html', {'form': form, 'especialidade': especialidade})


def excluir_especialidade(request, pk):
    especialidade = get_object_or_404(Especialidade, pk=pk)
    
    if request.method == 'POST':
        especialidade.delete()
        return redirect('listar-especialidade')  
    
    return render(request, 'paginasweb/confirmar_exclusao.html', {'especialidade': especialidade})

class EspecialidadeCreate(LoginRequiredMixin, CreateView):
    model = Especialidade
    fields = ['nome']  
    template_name = 'paginasweb/forms.html'
    success_url = '/especialidade/listar/'

class EspecialidadeList(ListView):
    model = Especialidade
    template_name = 'paginasweb/especialidade.html'  
    context_object_name = 'especialidades'  

class MedicoCreate(LoginRequiredMixin, CreateView):
    model = Medico
    fields = ['nome', 'crm', 'especialidade']  
    template_name = 'paginasweb/forms.html'
    success_url = '/medico/listar/'

class MedicoList(ListView):
    model = Medico
    template_name = 'paginasweb/medico.html'
    context_object_name = 'medicos'

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'telefone', 'cpf']
    template_name = 'paginasweb/forms.html'
    success_url = '/paciente/listar/'

class PacienteList(ListView):
    model = Paciente
    template_name = 'paginasweb/paciente.html'
    context_object_name = 'pacientes'

class ConsultaCreate(LoginRequiredMixin, CreateView):
    model = Consulta
    fields = ['paciente', 'medico', 'data', 'hora', 'observacoes', 'status']
    template_name = 'paginasweb/forms.html'
    success_url = '/consulta/listar/'

class ConsultaList(ListView):
    model = Consulta
    template_name = 'paginasweb/consulta.html'
    context_object_name = 'consultas'
