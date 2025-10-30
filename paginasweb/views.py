from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group

from .models import Especialidade, Medico, Paciente, Consulta
from .forms import EspecialidadeForm, UsuarioCadastroForm


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginasweb/forms.html'
    success_url = reverse_lazy('autenticar')
    extra_context = {'titulo': 'Registro de usuários', 'botao': 'Cadastrar'}


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
    fields = ['nome', 'descricao']  
    template_name = 'paginasweb/forms.html'
    success_url = '/especialidade/listar/'
    extra_context = {'titulo': 'Cadastrar Especialidade', 'botao': 'Salvar'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return redirect(self.success_url)

class EspecialidadeList(LoginRequiredMixin, ListView):
    model = Especialidade
    template_name = 'paginasweb/especialidade.html'  
    context_object_name = 'especialidades'  
    def get_queryset(self):
        return Especialidade.objects.filter(usuario=self.request.user)

class EspecialidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Especialidade
    fields = ['nome', 'descricao']
    template_name = 'paginasweb/forms.html'
    success_url = '/especialidade/listar/'
    extra_context = {'titulo': 'Editar Especialidade', 'botao': 'Salvar'}

    def get_queryset(self):
        return Especialidade.objects.filter(usuario=self.request.user)

class EspecialidadeDelete(LoginRequiredMixin, DeleteView):
    model = Especialidade
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/especialidade/listar/'
    extra_context = {'titulo': 'Excluir Especialidade', 'botao': 'Excluir'}

    def get_queryset(self):
        return Especialidade.objects.filter(usuario=self.request.user)

class MedicoCreate(LoginRequiredMixin, CreateView):
    model = Medico
    fields = ['nome', 'crm', 'especialidade']  
    template_name = 'paginasweb/forms.html'
    success_url = '/medico/listar/'
    extra_context = {'titulo': 'Cadastrar Médico', 'botao': 'Salvar'}

    def form_valid(self, form):
        # Garante que o médico pertence ao usuário autenticado
        obj = form.save(commit=False)
        if hasattr(self.request.user, 'medico') and self.request.user.medico.pk != obj.pk:
            # Usuário já possui um perfil de médico
            form.add_error(None, 'Você já possui um cadastro de médico.')
            return self.form_invalid(form)
        obj.usuario = self.request.user
        obj.save()
        return redirect(self.success_url)


class MedicoList(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'paginasweb/medico.html'
    context_object_name = 'medicos'
    def get_queryset(self):
        return Medico.objects.filter(usuario=self.request.user)

from django.views.generic import UpdateView, DeleteView

class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = Medico
    fields = ['nome', 'crm', 'especialidade']
    template_name = 'paginasweb/forms.html'
    success_url = '/medico/listar/'
    extra_context = {'titulo': 'Editar Médico', 'botao': 'Salvar'}

    def get_queryset(self):
        # Restringe edição ao dono do registro
        return Medico.objects.filter(usuario=self.request.user)

class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/medico/listar/'
    extra_context = {'titulo': 'Excluir Médico', 'botao': 'Excluir'}

    def get_queryset(self):
        return Medico.objects.filter(usuario=self.request.user)

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'telefone', 'cpf']
    template_name = 'paginasweb/forms.html'
    success_url = '/paciente/listar/'
    extra_context = {'titulo': 'Cadastrar Paciente', 'botao': 'Salvar'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        if hasattr(self.request.user, 'paciente') and self.request.user.paciente.pk != obj.pk:
            form.add_error(None, 'Você já possui um cadastro de paciente.')
            return self.form_invalid(form)
        obj.usuario = self.request.user
        obj.save()
        return redirect(self.success_url)

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'paginasweb/paciente.html'
    context_object_name = 'pacientes'
    def get_queryset(self):
        return Paciente.objects.filter(usuario=self.request.user)

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nome', 'telefone', 'cpf']
    template_name = 'paginasweb/forms.html'
    success_url = '/paciente/listar/'
    extra_context = {'titulo': 'Editar Paciente', 'botao': 'Salvar'}

    def get_queryset(self):
        return Paciente.objects.filter(usuario=self.request.user)

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/paciente/listar/'
    extra_context = {'titulo': 'Excluir Paciente', 'botao': 'Excluir'}

    def get_queryset(self):
        return Paciente.objects.filter(usuario=self.request.user)

class ConsultaCreate(LoginRequiredMixin, CreateView):
    model = Consulta
    fields = ['paciente', 'medico', 'data', 'hora', 'observacoes', 'status']
    template_name = 'paginasweb/forms.html'
    success_url = '/consulta/listar/'
    extra_context = {'titulo': 'Agendar Consulta', 'botao': 'Salvar'}

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Restringe as escolhas ao usuário quando aplicável
        if hasattr(self.request.user, 'paciente'):
            form.fields['paciente'].queryset = Paciente.objects.filter(usuario=self.request.user)
        if hasattr(self.request.user, 'medico'):
            form.fields['medico'].queryset = Medico.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        # Garante que o usuário só cria consultas vinculadas a ele
        paciente = form.cleaned_data.get('paciente')
        medico = form.cleaned_data.get('medico')
        user = self.request.user
        if hasattr(user, 'paciente') and paciente.usuario != user:
            form.add_error('paciente', 'Você só pode agendar para seu próprio cadastro.')
            return self.form_invalid(form)
        if hasattr(user, 'medico') and medico.usuario != user:
            form.add_error('medico', 'Você só pode agendar com seu próprio cadastro de médico.')
            return self.form_invalid(form)
        return super().form_valid(form)

class ConsultaList(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'paginasweb/consulta.html'
    context_object_name = 'consultas'
    def get_queryset(self):
        user = self.request.user
        return Consulta.objects.filter(
            Q(paciente__usuario=user) | Q(medico__usuario=user)
        )

class ConsultaUpdate(LoginRequiredMixin, UpdateView):
    model = Consulta
    fields = ['paciente', 'medico', 'data', 'hora', 'observacoes', 'status']
    template_name = 'paginasweb/forms.html'
    success_url = '/consulta/listar/'
    extra_context = {'titulo': 'Editar Consulta', 'botao': 'Salvar'}

    def get_queryset(self):
        user = self.request.user
        return Consulta.objects.filter(Q(paciente__usuario=user) | Q(medico__usuario=user))

class ConsultaDelete(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'paginasweb/confirmar_exclusao.html'
    success_url = '/consulta/listar/'
    extra_context = {'titulo': 'Excluir Consulta', 'botao': 'Excluir'}

    def get_queryset(self):
        user = self.request.user
        return Consulta.objects.filter(Q(paciente__usuario=user) | Q(medico__usuario=user))
