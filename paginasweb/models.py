from django.db import models

# Todas as classes DEVEM ter a herança para a classe Model que está dentro de "models"
# class SuaClasse(models.Model):
#   atributo = models.TipoDeAtributo(propriedade1=valor1, p2="v2", p3=v3)

# Depois de criar as classes, defina os atributos e seus tipos
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-types

# Cada campo tem suas propriedades, que estão disponíveis em
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-options


from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(default="Sem descrição") 

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=50)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
