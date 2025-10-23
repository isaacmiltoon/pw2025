from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Especialidade, Medico, Paciente, Consulta
from .forms import EspecialidadeForm  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
from django.urls import reverse_lazy

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/paciente/listar/'

class ConsultaDelete(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/consulta/listar/'
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Especialidade, Medico, Paciente, Consulta
from .forms import EspecialidadeForm  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
from django.urls import reverse_lazy


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginasweb/forms.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Registro de usuários'}


    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Paciente')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        # Retorna a URL de sucesso
        return url



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

from django.views.generic import UpdateView, DeleteView

class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = Medico
    fields = ['nome', 'crm', 'especialidade']
    template_name = 'paginasweb/forms.html'
    success_url = '/medico/listar/'

class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/medico/listar/'

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
