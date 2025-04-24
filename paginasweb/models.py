from django.db import models

# Todas as classes DEVEM ter a herança para a classe Model que está dentro de "models"
# class SuaClasse(models.Model):
#   atributo = models.TipoDeAtributo(propriedade1=valor1, p2="v2", p3=v3)

# Depois de criar as classes, defina os atributos e seus tipos
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-types

# Cada campo tem suas propriedades, que estão disponíveis em
# https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-options


class Campus(models.Model):
    nome = models.CharField(max_length=100)
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class TipoSolicitacao(models.Model):
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    prazo_externo = models.CharField(max_length=250)
    prazo_externo_dias = models.PositiveSmallIntegerField(default=0, help_text="Informe o prazo em dias que a solicitação leva para ser resolvida.")
    prazo_interno = models.CharField(max_length=250)
    prazo_interno_dias = models.PositiveSmallIntegerField(default=0)
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class Status(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.PositiveSmallIntegerField()
    pode_editar = models.BooleanField(help_text="Marque essa opção se for permitido atualizar a solicição com este Status.")
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matrícula = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=14)
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class Servidor(models.Model):
    nome = models.CharField(max_length=100)
    siape = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class Solicitacao(models.Model):
    solicitado_por = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    turma = models.CharField(max_length=100)
    tipo_solicitação = models.ForeignKey(TipoSolicitacao, on_delete=models.PROTECT)
    justificativa = models.TextField()
    cadastrado_em = models.DateTimeField(auto_now_add=True)


class Historico(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)