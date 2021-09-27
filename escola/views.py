from rest_framework import viewsets, generics
from escola import models as escola_model
from .serializer import AlunoSerializer, CursoSerializer, ListaAlunosMatriculadosSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """
        Exibindo todos os Alunos(as)
    """
    queryset = escola_model.Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """
        Exibindo todos os Cursos
    """
    queryset = escola_model.Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """
        Exibindo todas os Matriculas
    """
    queryset = escola_model.Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAlunos(generics.ListAPIView):
    """
        Listando as matrículas do(a) aluno(a)
    """
    def get_queryset(self):
            queryset = escola_model.Matricula.objects.filter(aluno_id=self.kwargs['pk'])
            return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """
        Listando alunos e alunas matriculados em um curso
    """
    def get_queryset(self):
        queryset = escola_model.Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

