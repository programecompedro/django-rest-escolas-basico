from rest_framework import serializers
from escola import models as escola_model

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = escola_model.Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_de_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = escola_model.Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = escola_model.Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = escola_model.Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model=escola_model.Matricula
        fields = ['aluno_nome']