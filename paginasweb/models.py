from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(default="Sem descrição")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='especialidades', null=True, blank=True)
    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medico')

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paciente')

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=50)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
