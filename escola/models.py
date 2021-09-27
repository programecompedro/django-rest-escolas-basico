from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome}'

class Curso(models.Model):
    OPCOES = (
        ('B', 'Básico'),
        ('A', 'Avançado'),
        ('I', 'Intermediário')
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255)
    codigo_curso = models.CharField(max_length=10)
    nivel = models.CharField(max_length=1, choices=OPCOES, blank=False, 
    null=False, default='B')

    def __str__(self):
        return f'{self.descricao}'

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    aluno = models.ForeignKey("escola.Aluno", on_delete=models.CASCADE)
    curso = models.ForeignKey("escola.Curso", on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')